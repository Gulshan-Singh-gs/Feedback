## 2024-06-08 - Unoptimized Favicon Bottleneck
**Learning:** The favicon in this repository was surprisingly large (329KB) and unoptimized, acting as a hidden network bottleneck during initial page load. Unoptimized static assets like favicons are low-hanging fruit for measurable payload reduction.
**Action:** Always check the size of static assets like images and favicons. Use tools like Pillow to compress them into appropriate sizes (e.g., 64x64 for favicons) and modern formats when optimizing load times.
