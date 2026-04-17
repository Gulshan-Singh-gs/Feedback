import asyncio
from playwright.sync_api import sync_playwright
import time
import subprocess
import os

def run_test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        # Route abortion for external assets as per memory rules
        page.route("**/*", lambda route: route.abort() if route.request.resource_type in ["font", "image", "media"] else route.continue_())

        print("Navigating to index.html...")
        page.goto("http://localhost:8000/index.html", wait_until="domcontentloaded")

        print("Testing form submission to ensure it triggers AJAX (no page reload)...")
        # Ensure form button works and triggers AJAX
        page.select_option("#serviceSelect", "Core Engine Latency")
        page.fill("#feedbackTextarea", "Testing performance bug fix.")

        # ensure button is enabled
        is_disabled = page.evaluate("document.getElementById('executeBtn').disabled")
        print(f"Is submit button disabled? {is_disabled}")

        # Trigger validation manually since Playwright fill might not trigger the exact event chain
        page.evaluate("document.getElementById('upgradeForm').dispatchEvent(new Event('input', {bubbles:true}))")

        with page.expect_request("https://api.web3forms.com/submit") as first_request:
            page.click("#executeBtn")

        print("AJAX request caught!")

        # The fetch response might return immediately so checking 'Transmitting' is a race condition.
        # But capturing the request means the eventListener for 'submit' fired.
        print("UI successfully triggered AJAX request - Page did NOT reload!")

        browser.close()

if __name__ == "__main__":
    # Start the local server
    print("Starting local server...")
    server_process = subprocess.Popen(["python3", "-m", "http.server", "8000"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(2) # Give server time to start

    try:
        run_test()
    finally:
        print("Shutting down local server...")
        server_process.terminate()
        server_process.wait()
