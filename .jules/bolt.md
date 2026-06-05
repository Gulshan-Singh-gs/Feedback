## 2024-06-05 - Unoptimized Assets Blocking Initial Render
**Learning:** High-resolution unoptimized static assets (like a 329KB `fevicon.png`) unnecessarily bloat the initial network payload and can delay page rendering, violating the principle that "every millisecond counts".
**Action:** Always check basic asset sizes (especially images and favicons) and compress them appropriately for their intended display dimensions. For simple optimization without node pipelines, Python's `Pillow` library is an effective ad-hoc tool.
