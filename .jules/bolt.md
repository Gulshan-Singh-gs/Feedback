## 2024-05-24 - Large Favicon Image Optimization
**Learning:** Found an unoptimized 509x511 `fevicon.png` weighing ~330KB. For a frontend-centric app, loading an unoptimized favicon is a direct performance loss (unnecessary network payload) without any visual benefit since favicons are rendered small (usually 16x16 or 32x32).
**Action:** Always verify the dimensions and file sizes of static assets, specifically `favicon.png` or `fevicon.png`. Use `Pillow` to resize and compress static images.
