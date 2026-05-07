## 2024-05-07 - Unoptimized Static Assets
**Learning:** Found a massive `fevicon.png` (322KB, 509x511 resolution) being served directly without any sizing or compression. In this frontend-centric project, unoptimized static assets significantly increase the initial network payload and delay page load times.
**Action:** Always check for improperly sized image assets (especially favicons) and compress them appropriately using tools like Pillow to reduce network payload and improve perceived performance.
