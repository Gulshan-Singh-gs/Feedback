## 2026-06-12 - Huge Unoptimized Assets
**Learning:** Found a 329KB unoptimized 509x511 favicon (`fevicon.png`) in the repo. The codebase doesn't have an automated asset build pipeline or a `package.json`, which implies static assets rely entirely on manual optimization.
**Action:** Always verify the size and resolution of seemingly harmless static assets like favicons when looking for easy frontend wins, and use Python (e.g., Pillow) for resizing and compressing when node tools aren't present.
