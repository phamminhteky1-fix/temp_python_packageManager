import subprocess
import sys
import importlib

# Track packages installed during this session
installed_temp = []

def ensure_package(package_name):
    try:
        importlib.import_module(package_name)
    except ImportError:
        print(f"📦 Installing {package_name} temporarily...")
        print("DO NOT PRESS CTRL + C!!!")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        installed_temp.append(package_name)

def cleanup_packages():
    for pkg in installed_temp:
        print(f"🧹 Uninstalling {pkg}...")
        print("DO NOT PRESS CTRL + C!!!")
        subprocess.check_call([sys.executable, "-m", "pip", "uninstall", "-y", pkg])
