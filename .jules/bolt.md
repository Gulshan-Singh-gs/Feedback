## 2026-06-15 - Unoptimized Favicons
**Learning:** Favicons in the root directory can be unexpectedly large (~322KB) if unoptimized, causing unnecessary network overhead on every page load.
**Action:** Always check static asset sizes, especially globally loaded icons like favicons, and compress them using tools like Pillow before shipping.
