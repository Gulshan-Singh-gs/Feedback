## 2024-06-13 - Unoptimized Favicon Image Optimization
**Learning:** The project uses a massive unoptimized image (`fevicon.png`, 329KB, 509x511) as a favicon. Since the `favicon` size needed for browsers is typically very small (e.g. 32x32 to 64x64), a large PNG significantly hurts initial load time and wastes bandwidth without providing any visual benefit.
**Action:** Always check the size and dimensions of images used for favicons or minor UI elements. Optimize them to standard sizes using Pillow to drastically reduce their footprint.
