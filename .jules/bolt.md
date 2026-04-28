## 2024-10-24 - Remove duplicate DOM bindings
**Learning:** Found an anti-pattern in the codebase where redundant `<script>` blocks were added outside the `DOMContentLoaded` event, causing duplicate DOM bindings for form elements (`serviceSelect` and `feedbackTextarea`). This caused memory overhead and redundant event listeners.
**Action:** Always scan for redundant or duplicate DOM query and event listener logic during initialization, ensuring all such handlers are consolidated within the primary initialization block (e.g., `DOMContentLoaded`).
