
## 2024-04-18 - Event Delegation & Code Duplication
**Learning:** Found duplicate event listeners attached to the same components natively and manually which effectively doubled the number of active event listeners and added slightly to the JS Heap size. Combining these manually-added listeners and implementing simple event delegation for the inputs resulted in a halving of JSEventListeners.
**Action:** Always check vanilla JS scripts to ensure there is no duplicate logic or code, and look out for multiple element event listener attachments that can be easily simplified via event delegation on a common parent.
