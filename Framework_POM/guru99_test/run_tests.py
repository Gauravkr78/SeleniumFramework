import subprocess
import sys

def main():
    print("🚀 Running Guru99 Selenium Tests...")

    print("\n📊 Running with pytest...")
    subprocess.call([sys.executable, "-m", "pytest", "tests/test_guru99.py", "-v"])

if __name__ == "__main__":
    main()
