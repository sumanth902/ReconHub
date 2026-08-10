from core.detector import detect_target
from core.module_manager import get_modules

from services.whois_lookup import get_whois
from services.dns_lookup import get_dns_records
from services.subdomain_lookup import get_subdomains
from services.wappalyzer import get_technologies
from services.security_headers import get_security_headers
from services.ssl_lookup import get_ssl_info
from services.robots_lookup import get_robots
from services.sitemap_lookup import get_sitemap
from services.wayback_lookup import get_wayback
from services.google_dorks import get_google_dorks
from services.port_scanner import scan_ports
from services.sherlock_lookup import search_username
from services.export_json import export_json
from services.http_fingerprint import http_fingerprint
from services.email_security import email_security
from exports.pdf_export import export_pdf
from services.risk_score import calculate_risk
from services.geoip_lookup import get_geoip
from services.screenshot import capture_screenshot
from services.save_history import save_scan
from services.cve_lookup import get_cves
def start_recon(target):

    target_type = detect_target(target)

    selected_modules = get_modules(target_type)
    print(selected_modules)

    results = {
        "target": target,
        "target_type": target_type,
        "modules": selected_modules
    }

    if "WHOIS" in selected_modules:
        results["whois"] = get_whois(target)

    if "DNS" in selected_modules:
        results["dns"] = get_dns_records(target)

    if "Subdomains" in selected_modules:
        results["subdomains"] = get_subdomains(target)

    if "Wappalyzer" in selected_modules:
        results["technologies"] = get_technologies(target)

    if results.get("technologies"):
        print("Looking up CVEs...")
    results["cves"] = get_cves(results["technologies"])

    if "Security Headers" in selected_modules:
        print("Running Security Headers...")
        results["security_headers"] = get_security_headers(target)
        print(results["security_headers"])

    if target_type == "domain":
        results["ssl"] = get_ssl_info(target)

    if target_type == "domain":
        results["robots"] = get_robots(target)

    if target_type == "domain":
        results["sitemap"] = get_sitemap(target)  

    if target_type == "domain":
        results["wayback"] = get_wayback(target)

    if target_type == "domain":
        results["geoip"] = get_geoip(target)

    if target_type == "domain":
        print("Capturing Website Screenshot...")
        results["screenshot"] = capture_screenshot(target)

    if "Google Dorks" in selected_modules:
        results["google_dorks"] = get_google_dorks(target)

    if "Open Ports" in selected_modules:
        print("Scanning ports...")
        results["ports"] = scan_ports(target)
        print(results["ports"])
    print(results)

    if "Sherlock" in selected_modules:
        results["sherlock"] = search_username(target)
        print(results["sherlock"])
        print(results["sherlock"])

    if "HTTP Fingerprint" in selected_modules:
        results["http"] = http_fingerprint(target)

        # Calculate Risk Score
    results["risk"] = calculate_risk(results)
    print(results["risk"])

    results["json_report"] = export_json(results)
    results["email_security"] = email_security(target)
    results["pdf_report"] = export_pdf(results)
    save_scan(results)
    return results
