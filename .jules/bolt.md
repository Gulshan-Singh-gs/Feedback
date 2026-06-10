
## 2024-06-10 - Unoptimized Static Assets (Favicon)
**Learning:** Found an unoptimized `fevicon.png` (329KB). Large unoptimized static assets block page load and consume unnecessary bandwidth. It's important to check the size of simple static assets.
**Action:** Always verify image asset sizes, particularly for items like favicons, and compress them using `Pillow` or similar tools with appropriate dimensions and optimization flags to minimize initial load payload.
