from services.security_headers import get_security_headers
if "Security Headers" in selected_modules:
    results["security_headers"] = get_security_headers(target)