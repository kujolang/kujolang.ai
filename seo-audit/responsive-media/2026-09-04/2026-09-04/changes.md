# Implemented changes

Audit date: 2026-09-04

- Added deterministic 640 px, 960 px, and 1280 px WebP candidates for generated local images without modifying committed source media.
- Added width-descriptor `srcset` and layout-accurate `sizes` attributes to local featured and listing images; remote images remain untouched.
- Integrated responsive generation into GitHub Pages and local preview builds.
- Added unit coverage for deterministic generation and a rendered-site contract that verifies every advertised candidate exists.
- Preserved titles, descriptions, canonicals, schema, content, crawler policy, and source-repository calls to action.
