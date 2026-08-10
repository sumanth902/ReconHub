import subprocess

def search_username(username):
    return "Sherlock is working!"

    result = subprocess.run(
        [
            "sherlock",
            username,
            "--print-found",
            "--no-color"
        ],
        capture_output=True,
        text=True
    )

    print("STDOUT:")
    print(result.stdout)

    print("STDERR:")
    print(result.stderr)

    return result.stdout + result.stderr