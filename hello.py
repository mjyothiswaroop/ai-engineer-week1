import platform
import sys

def describe_machine(name: str) -> str:
    return f"Hello {name}, running Python {platform.python_version()} on {platform.system()}"

if __name__ == "__main__":
    # Check if a name argument was passed from the terminal
    if len(sys.argv) > 1:
        # Grab the first argument provided after the script name
        user_name = sys.argv[1]
    else:
        # Fallback default if no argument is provided
        user_name = "future AI engineer"

    print(describe_machine(user_name))