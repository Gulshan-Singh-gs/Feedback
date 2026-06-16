## 2026-06-16 - Massive Unoptimized Favicon Bottleneck
**Learning:** The project included a ~329KB raw image as a favicon, creating a massive unnecessary network payload blocking page load.
**Action:** Always resize favicons to appropriate dimensions (e.g., 64x64) and apply compression using Pillow when working on static assets without a Node build pipeline.
