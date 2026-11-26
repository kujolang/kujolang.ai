"""A failed robots fetch must not be reported as a site-owner disallow rule."""
import importlib.util
import io
from pathlib import Path
import unittest
from unittest.mock import patch
from urllib.error import HTTPError

spec = importlib.util.spec_from_file_location('probe_site', Path(__file__).parents[1] / 'scripts/probe_site.py')
probe = importlib.util.module_from_spec(spec)
spec.loader.exec_module(probe)

class RobotsFetchTests(unittest.TestCase):
    def rows(self, body=None, error=None):
        response = io.BytesIO(body or b'')
        response.status = 200
        with patch.object(probe, 'request', return_value={'status': 200}), patch.object(
            probe.urllib.request, 'urlopen', return_value=response, side_effect=error
        ) as fetch:
            rows, _ = probe.crawler_access('https://example.test', 'after', '/compare/')
            self.assertIn('KujolangSEOAudit', fetch.call_args.args[0].get_header('User-agent'))
            return rows

    def test_explicit_allow(self):
        self.assertTrue(all(r['robots_allowed'] == 'yes' for r in self.rows(b'User-agent: *\nAllow: /\n')))

    def test_real_disallow(self):
        self.assertTrue(all(r['robots_allowed'] == 'no' for r in self.rows(b'User-agent: *\nDisallow: /compare/\n')))

    def test_blocked_fetch_is_unknown(self):
        error = HTTPError('https://example.test/robots.txt', 403, 'Forbidden', {}, None)
        self.assertTrue(all(r['robots_allowed'] == 'unknown' for r in self.rows(error=error)))

    def test_network_failure_is_unknown(self):
        self.assertTrue(all(r['robots_allowed'] == 'unknown' for r in self.rows(error=TimeoutError())))


class RedirectTests(unittest.TestCase):
    def test_checks_endpoint_status_canonical_target_and_query(self):
        def response(url, _user_agent):
            overrides = {
                'https://example.test/sitemap.xml': (404, url),
                'https://example.test/compare/?audit=1': (200, 'https://example.test/compare/'),
                'https://example.test/compare': (200, 'https://example.test/'),
                'https://example.test/robots.txt': (200, 'https://example.test.invalid/robots.txt'),
                'https://example.test/compare.html': (404, url),
            }
            status, final_url = overrides.get(url, (200, url))
            chain = [{'status': 308}] if url.endswith('/compare') else []
            return {'status': status, 'final_url': final_url, 'chain': chain, 'error': ''}

        with patch.object(probe, 'request', side_effect=response):
            rows, _ = probe.redirects('https://example.test', 'after', '/compare/', False, None)
        by_variant = {row['source_variant']: row for row in rows}
        self.assertIn('expected 200', by_variant['sitemap']['issues'])
        self.assertIn('query string changed or missing', by_variant['query string']['issues'])
        self.assertEqual(by_variant['nested no trailing slash']['canonical_target'], 'no')
        self.assertEqual(by_variant['robots']['canonical_target'], 'no')
        self.assertEqual(by_variant['nested canonical']['issues'], '')
        self.assertEqual(by_variant['flat HTML alias']['issues'], '')


if __name__ == '__main__':
    unittest.main()
