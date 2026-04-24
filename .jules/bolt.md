## 2026-04-24 - Duplicate Event Bindings in index.html
**Learning:** Found a major architectural quirk where `index.html` contained a duplicated set of identical form initialization scripts outside of the `DOMContentLoaded` block. This caused redundant event listeners (JSEventListeners = 7 initially) and broke initialization if variables referenced undefined objects due to timing issues.
**Action:** When auditing pure HTML/JS frontend apps, always check for trailing `<script>` blocks or globally scoped bindings that duplicate correctly scoped logic inside `DOMContentLoaded`.
