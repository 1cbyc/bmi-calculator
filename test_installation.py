#!/usr/bin/env python3
"""
Test script to verify BMI Calculator installation
"""

def test_imports():
    """Test if all required modules can be imported"""
    try:
        import customtkinter as ctk
        print("✓ CustomTkinter imported successfully")
        return True
    except ImportError as e:
        print(f"✗ Failed to import CustomTkinter: {e}")
        print("Please install dependencies with: pip install -r requirements.txt")
        return False

def test_settings():
    """Test if settings.py can be imported"""
    try:
        import settings
        print("✓ Settings imported successfully")
        return True
    except ImportError as e:
        print(f"✗ Failed to import settings: {e}")
        return False

def test_bmi_calculation():
    """Test BMI calculation logic"""
    try:
        # Simple BMI calculation test
        weight_kg = 70
        height_meter = 1.75
        bmi = round(weight_kg / height_meter ** 2, 2)
        expected_bmi = 22.86
        
        if abs(bmi - expected_bmi) < 0.01:
            print("✓ BMI calculation working correctly")
            return True
        else:
            print(f"✗ BMI calculation error: got {bmi}, expected {expected_bmi}")
            return False
    except Exception as e:
        print(f"✗ BMI calculation test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("Testing BMI Calculator installation...")
    print("-" * 40)
    
    tests = [
        test_imports,
        test_settings,
        test_bmi_calculation
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("-" * 40)
    print(f"Tests passed: {passed}/{total}")
    
    if passed == total:
        print("🎉 All tests passed! You can now run the BMI calculator with:")
        print("python bmi.py")
    else:
        print("❌ Some tests failed. Please check the errors above.")
    
    return passed == total

if __name__ == "__main__":
    main() 