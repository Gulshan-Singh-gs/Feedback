## 2026-04-27 - Remove Duplicate DOM Bindings
**Learning:** Duplicate initialization logic (DOM queries and listeners) outside of DOMContentLoaded not only increases the number of active event listeners but also masks bugs within the primary initialization block.
**Action:** Ensure single point of initialization within DOMContentLoaded and remove redundant fallback scripts.
