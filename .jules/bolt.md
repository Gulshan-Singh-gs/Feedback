## 2026-04-21 - Remove Redundant Event Listeners
**Learning:** Fixing broken DOM ID references allowed us to delete duplicated global event listeners, which directly reduced memory overhead (`JSHeapUsedSize`) and reduced the `JSEventListeners` metric.
**Action:** When auditing a frontend project without a build step or framework, check for redundant global listeners appended below structured `DOMContentLoaded` listeners.
