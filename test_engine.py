from core.engine import start_recon

result = start_recon("google.com")

print("Target :", result["target"])
print("Type   :", result["target_type"])

print("\nModules to Run:")

for module in result["modules"]:
    print("✓", module)