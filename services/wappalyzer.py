import requests
from bs4 import BeautifulSoup


def detect_server(headers):
    tech = []

    server = headers.get("Server", "").lower()
    powered = headers.get("X-Powered-By", "").lower()

    if "nginx" in server:
        tech.append(("Web Server", "Nginx"))

    if "apache" in server:
        tech.append(("Web Server", "Apache"))

    if "iis" in server:
        tech.append(("Web Server", "Microsoft IIS"))

    if "cloudflare" in server or "cf-ray" in headers:
        tech.append(("CDN", "Cloudflare"))

    if "express" in powered:
        tech.append(("Backend", "Express.js"))

    if "php" in powered:
        tech.append(("Backend", "PHP"))

    if "asp.net" in powered:
        tech.append(("Backend", "ASP.NET"))

    return tech


def detect_html(html):
    tech = []

    html = html.lower()

    # ---------------- CMS ----------------

    if "wp-content" in html:
        tech.append(("CMS", "WordPress"))

    if "drupal-settings-json" in html:
        tech.append(("CMS", "Drupal"))

    if "joomla" in html:
        tech.append(("CMS", "Joomla"))

    # ---------------- CSS ----------------

    if "bootstrap" in html:
        tech.append(("CSS", "Bootstrap"))

    if "tailwind" in html:
        tech.append(("CSS", "Tailwind CSS"))

    if "bulma" in html:
        tech.append(("CSS", "Bulma"))

    # ---------------- Frameworks ----------------

    if "__next_data__" in html:
        tech.append(("Framework", "Next.js"))

    if "_nuxt" in html:
        tech.append(("Framework", "Nuxt.js"))

    if "react" in html:
        tech.append(("Framework", "React"))

    if "vue" in html:
        tech.append(("Framework", "Vue.js"))

    if "angular" in html:
        tech.append(("Framework", "Angular"))

    # ---------------- JavaScript ----------------

    if "jquery" in html:
        tech.append(("JavaScript", "jQuery"))

    # ---------------- Build Tools ----------------

    if "webpack" in html:
        tech.append(("Build Tool", "Webpack"))

    if "vite" in html:
        tech.append(("Build Tool", "Vite"))

    # ---------------- Analytics ----------------

    if "googletagmanager" in html:
        tech.append(("Analytics", "Google Tag Manager"))

    if "google-analytics" in html:
        tech.append(("Analytics", "Google Analytics"))

    if "gtag(" in html:
        tech.append(("Analytics", "Google Analytics"))

    if "hotjar" in html:
        tech.append(("Analytics", "Hotjar"))

    # ---------------- Fonts ----------------

    if "fonts.googleapis.com" in html:
        tech.append(("Fonts", "Google Fonts"))

    if "font-awesome" in html:
        tech.append(("Icons", "Font Awesome"))

    # ---------------- Security ----------------

    if "recaptcha" in html:
        tech.append(("Security", "Google reCAPTCHA"))

    if "hcaptcha" in html:
        tech.append(("Security", "hCaptcha"))

    return tech


def detect_scripts(soup):
    tech = []

    scripts = " ".join(
        script.get("src", "")
        for script in soup.find_all("script")
    ).lower()

    if "react" in scripts:
        tech.append(("Framework", "React"))

    if "next" in scripts:
        tech.append(("Framework", "Next.js"))

    if "vue" in scripts:
        tech.append(("Framework", "Vue.js"))

    if "angular" in scripts:
        tech.append(("Framework", "Angular"))

    if "jquery" in scripts:
        tech.append(("JavaScript", "jQuery"))

    if "bootstrap" in scripts:
        tech.append(("CSS", "Bootstrap"))

    if "tailwind" in scripts:
        tech.append(("CSS", "Tailwind CSS"))

    if "webpack" in scripts:
        tech.append(("Build Tool", "Webpack"))

    if "vite" in scripts:
        tech.append(("Build Tool", "Vite"))

    return tech


def detect_meta(soup):
    tech = []

    generator = ""

    tag = soup.find("meta", attrs={"name": "generator"})

    if tag:
        generator = tag.get("content", "").lower()

    if "wordpress" in generator:
        tech.append(("CMS", "WordPress"))

    if "drupal" in generator:
        tech.append(("CMS", "Drupal"))

    if "joomla" in generator:
        tech.append(("CMS", "Joomla"))

    return tech


def get_technologies(domain):

    try:

        url = f"https://{domain}"

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=15
        )

        html = response.text

        soup = BeautifulSoup(html, "html.parser")

        technologies = []

        technologies.extend(detect_server(response.headers))
        technologies.extend(detect_html(html))
        technologies.extend(detect_scripts(soup))
        technologies.extend(detect_meta(soup))

        technologies = sorted(set(technologies))

        return technologies

    except Exception as e:
        print("Technology Error:", e)
        return []