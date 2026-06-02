## 2024-06-02 - Manual Asset Optimization for Buildless Repos
**Learning:** In repositories without a Node-based build pipeline (like Vite or Webpack), large static assets (like favicons) can slip into production unoptimized, causing significant unnecessary network payload.
**Action:** Always check static assets (images, favicons) in buildless repositories and use manual optimization tools like Python's Pillow to resize and compress them before shipping.
