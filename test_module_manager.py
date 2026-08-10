from core.module_manager import get_modules

targets = [
    "domain",
    "ip",
    "email",
    "username"
]

for t in targets:

    print(f"\nTarget Type : {t}")

    for module in get_modules(t):
        print("   ✓", module)