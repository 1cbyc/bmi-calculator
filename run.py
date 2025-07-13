#!/usr/bin/env python3
"""
BMI Calculator Pro Launcher
"""

import sys
import os

def main():
    """Launch the BMI Calculator application"""
    print("🚀 Starting BMI Calculator Pro...")
    
    try:
        # Check if CustomTkinter is available
        import customtkinter as ctk
        print("✅ CustomTkinter loaded successfully")
        
        # Import our modules
        from bmi import App
        print("✅ BMI Calculator modules loaded")
        
        # Start the application
        print("🎯 Launching GUI...")
        app = App()
        
    except ImportError as e:
        print(f"❌ Import Error: {e}")
        print("Please install dependencies with: pip install -r requirements.txt")
        input("Press Enter to exit...")
        sys.exit(1)
        
    except Exception as e:
        print(f"❌ Error starting application: {e}")
        print("Please check your Python installation and dependencies.")
        input("Press Enter to exit...")
        sys.exit(1)

if __name__ == "__main__":
    main() 