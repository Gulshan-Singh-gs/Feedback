## 2024-05-15 - Unoptimized Favicon Compression
**Learning:** Found an unoptimized `fevicon.png` static asset (322 KB) causing unnecessary network payload size.
**Action:** Optimized using Pillow library to resize from 509x511 to 64x64, yielding a 97% size reduction. Prioritize asset compression when no Node build pipeline exists.
