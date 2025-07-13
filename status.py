#!/usr/bin/env python3
"""
BMI Calculator Pro - Status Check
"""

def check_status():
    """Check if all components are working"""
    print("🔍 BMI Calculator Pro - Status Check")
    print("=" * 40)
    
    # Check Python
    import sys
    print(f"✅ Python {sys.version[:3]} detected")
    
    # Check CustomTkinter
    try:
        import customtkinter as ctk
        print("✅ CustomTkinter imported successfully")
    except ImportError as e:
        print(f"❌ CustomTkinter import failed: {e}")
        return False
    
    # Check our modules
    try:
        from settings import *
        print("✅ Settings module working")
    except ImportError as e:
        print(f"❌ Settings import failed: {e}")
        return False
    
    try:
        from config import config
        print("✅ Configuration system working")
    except ImportError as e:
        print(f"❌ Config import failed: {e}")
        return False
    
    try:
        from utils import calculate_bmi, get_bmi_category
        print("✅ Utility functions working")
    except ImportError as e:
        print(f"❌ Utils import failed: {e}")
        return False
    
    # Test BMI calculation
    try:
        bmi = calculate_bmi(70, 170)
        category, color = get_bmi_category(bmi)
        print(f"✅ BMI calculation working: {bmi} ({category})")
    except Exception as e:
        print(f"❌ BMI calculation failed: {e}")
        return False
    
    # Test configuration
    try:
        color = config.get('theme.primary_color')
        print(f"✅ Configuration working: {color}")
    except Exception as e:
        print(f"❌ Configuration failed: {e}")
        return False
    
    print("\n🎉 All systems operational!")
    print("✅ BMI Calculator Pro is ready to use!")
    return True

if __name__ == "__main__":
    success = check_status()
    if success:
        print("\n🚀 To run the application:")
        print("  python bmi.py")
        print("  or")
        print("  python run.py")
    else:
        print("\n❌ Some components failed. Please check the errors above.") 