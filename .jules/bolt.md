## 2024-06-09 - Large Unoptimized Static Assets (Favicon)
**Learning:** Found a massive unoptimized static asset (a 329KB `fevicon.png` at 509x511) being served on the primary route. In this codebase, static assets can significantly balloon payload sizes due to lack of a build/optimization pipeline.
**Action:** When auditing frontend performance in similar repositories, always explicitly check the sizes and dimensions of static assets like images and favicons before looking at JS/CSS optimizations.
