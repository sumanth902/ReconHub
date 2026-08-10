from services.wappalyzer import get_technologies

domain = "react.dev"

result = get_technologies(domain)

print(result)