## 2024-05-14 - Unoptimized static image assets
**Learning:** This codebase includes large, unoptimized static assets (like a 329KB favicon) which needlessly consume bandwidth on critical page loads, as there is no Node-based build pipeline to automate asset optimization.
**Action:** When searching for performance wins, prioritize inspecting image and static asset file sizes. Use the `Pillow` library in Python to resize and compress these assets to deliver immediate, measurable network payload reductions with zero functionality risk.
