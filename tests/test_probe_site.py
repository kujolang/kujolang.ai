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

if __name__ == '__main__':
    unittest.main()
