#!/usr/bin/env python3
"""
BMI Calculator Pro - Installation Verification
"""

import sys
import os

def test_imports():
    """Test all module imports"""
    print("🔍 Testing module imports...")
    
    try:
        import customtkinter as ctk
        print("✅ CustomTkinter imported successfully")
    except ImportError as e:
        print(f"❌ CustomTkinter import failed: {e}")
        return False
    
    try:
        from settings import *
        print("✅ Settings imported successfully")
    except ImportError as e:
        print(f"❌ Settings import failed: {e}")
        return False
    
    try:
        from config import config
        print("✅ Configuration system imported successfully")
    except ImportError as e:
        print(f"❌ Config import failed: {e}")
        return False
    
    try:
        from utils import calculate_bmi, get_bmi_category
        print("✅ Utility functions imported successfully")
    except ImportError as e:
        print(f"❌ Utils import failed: {e}")
        return False
    
    return True

def test_calculations():
    """Test BMI calculations"""
    print("\n🧮 Testing BMI calculations...")
    
    try:
        from utils import calculate_bmi, get_bmi_category
        
        # Test normal BMI
        bmi = calculate_bmi(70, 170)
        category, color = get_bmi_category(bmi)
        print(f"✅ Normal BMI calculation: {bmi} ({category})")
        
        # Test underweight
        bmi = calculate_bmi(50, 170)
        category, color = get_bmi_category(bmi)
        print(f"✅ Underweight BMI calculation: {bmi} ({category})")
        
        # Test overweight
        bmi = calculate_bmi(90, 170)
        category, color = get_bmi_category(bmi)
        print(f"✅ Overweight BMI calculation: {bmi} ({category})")
        
        return True
    except Exception as e:
        print(f"❌ Calculation test failed: {e}")
        return False

def test_configuration():
    """Test configuration system"""
    print("\n⚙️ Testing configuration system...")
    
    try:
        from config import config
        
        # Test config loading
        primary_color = config.get('theme.primary_color')
        print(f"✅ Configuration loaded: {primary_color}")
        
        # Test config setting
        config.set('test.value', 'test')
        test_value = config.get('test.value')
        print(f"✅ Configuration setting: {test_value}")
        
        return True
    except Exception as e:
        print(f"❌ Configuration test failed: {e}")
        return False

def test_file_structure():
    """Test project file structure"""
    print("\n📁 Testing project structure...")
    
    required_files = [
        'bmi.py',
        'settings.py',
        'config.py',
        'utils.py',
        'requirements.txt',
        'README.md',
        'LICENSE',
        'setup.py'
    ]
    
    missing_files = []
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file}")
        else:
            print(f"❌ {file} (missing)")
            missing_files.append(file)
    
    if missing_files:
        print(f"\n⚠️ Missing files: {', '.join(missing_files)}")
        return False
    
    return True

def main():
    """Run all verification tests"""
    print("🚀 BMI Calculator Pro - Installation Verification")
    print("=" * 50)
    
    tests = [
        ("Module Imports", test_imports),
        ("BMI Calculations", test_calculations),
        ("Configuration System", test_configuration),
        ("File Structure", test_file_structure)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n📋 {test_name}")
        print("-" * 30)
        if test_func():
            passed += 1
        else:
            print(f"❌ {test_name} failed")
    
    print("\n" + "=" * 50)
    print(f"📊 Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Your BMI Calculator Pro is ready to use.")
        print("\nTo run the application:")
        print("  python bmi.py")
        print("  or")
        print("  python run.py")
    else:
        print("❌ Some tests failed. Please check the errors above.")
        return False
    
    return True

if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1) 