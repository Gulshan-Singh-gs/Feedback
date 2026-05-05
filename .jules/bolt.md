
## $(date +%Y-%m-%d) - CSS Transitions and Playwright Verification
**Learning:** When using Playwright to take screenshots of UI elements right after they change states (like a disabled button becoming enabled), the visual appearance might not match the internal DOM state because CSS transitions (like `opacity` or `transform` fading over 0.3s) have not yet completed. This can lead to false-negative code reviews where the code works but the screenshot looks visually wrong.
**Action:** Always include a small wait (`page.wait_for_timeout(1000)`) before taking a screenshot of a recently updated UI element to ensure all CSS transitions and animations have settled.
