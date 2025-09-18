import os
import sys


def main():
    print("Hello from rpi-management!")

    if len(sys.argv) > 1 and sys.argv[1] == "copy-programs":
        os.system("uv run src/copy-programs.py")
    
    if len(sys.argv) > 1 and sys.argv[1] == "write-env-file":
        os.system("uv run src/write-env-file.py")

    if len(sys.argv) > 1 and sys.argv[1] == "enable-programs":
        os.system("uv run src/enable-programs.py")

    if len(sys.argv) > 1 and sys.argv[1] == "update-programs":
        os.system("uv run src/update-programs.py")

if __name__ == "__main__":
    main()
