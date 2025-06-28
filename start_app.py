"""
GrainPalette Rice Classification App Launcher
This script provides an easy way to start the Streamlit application.
"""

import subprocess
import sys
import os
from pathlib import Path

def check_requirements():
    """Check if required files exist"""
    required_files = ['rice.keras', 'app.py']
    missing_files = []
    
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print("❌ Missing required files:")
        for file in missing_files:
            print(f"   - {file}")
        return False
    
    return True

def install_requirements():
    """Install required packages"""
    print("📦 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Requirements installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing requirements: {e}")
        return False

def run_tests():
    """Run system tests"""
    print("🧪 Running system tests...")
    try:
        result = subprocess.run([sys.executable, "test_system.py"], capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print("Warnings/Errors:")
            print(result.stderr)
        return result.returncode == 0
    except Exception as e:
        print(f"❌ Error running tests: {e}")
        return False

def start_app():
    """Start the Streamlit app"""
    print("🚀 Starting GrainPalette Rice Classification App...")
    try:
        subprocess.run(["streamlit", "run", "app.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error starting app: {e}")
        return False
    except FileNotFoundError:
        print("❌ Streamlit not found. Please install it first:")
        print("   pip install streamlit")
        return False
    
    return True

def main():
    """Main launcher function"""
    print("🌾 GrainPalette Rice Classification System")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists('app.py'):
        print("❌ Please run this script from the GrainPalette project directory")
        return
    
    # Check requirements
    if not check_requirements():
        print("\n❌ Cannot start app due to missing files")
        return
    
    # Install requirements
    print("\n1. Checking and installing requirements...")
    if not install_requirements():
        print("❌ Failed to install requirements")
        return
    
    # Run tests
    print("\n2. Running system tests...")
    if not run_tests():
        print("⚠️  Some tests failed, but continuing...")
    
    # Start the app
    print("\n3. Starting the application...")
    start_app()

if __name__ == "__main__":
    main()
