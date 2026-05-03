## 2024-05-18 - [Redundant Initializations]
**Learning:** Found redundant DOM bindings and global variable declarations outside the standard `DOMContentLoaded` wrapper in `index.html`. These cause unnecessary DOM querying and duplicate event listeners, wasting CPU cycles and JS heap. They were identical to those inside the wrapper.
**Action:** Remove duplicate/redundant global scripts that are meant to be enclosed in initialization wrappers to reduce unnecessary `addEventListener` calls and global variables. Always check the end of scripts for lingering loose logic.
