from playwright.sync_api import sync_playwright
import os


def capture_screenshot(domain):

    try:

        os.makedirs("static/screenshots", exist_ok=True)

        filename = f"{domain}.png"
        filepath = os.path.join("static", "screenshots", filename)

        with sync_playwright() as p:

            browser = p.chromium.launch(headless=True)

            page = browser.new_page(
                viewport={"width": 1366, "height": 768}
            )

            page.goto(
                f"https://{domain}",
                wait_until="domcontentloaded",
                timeout=60000
            )

            # Give the page a couple of seconds to finish rendering
            page.wait_for_timeout(2000)

            page.screenshot(
                path=filepath,
                full_page=True
            )

            browser.close()

        return filepath

    except Exception as e:
        print("Screenshot Error:", e)
        return None