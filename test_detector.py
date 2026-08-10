from core.detector import detect_target

tests = [
    "google.com",
    "8.8.8.8",
    "someone@gmail.com",
    "john_doe"
]

for target in tests:
    print(f"{target} --> {detect_target(target)}")