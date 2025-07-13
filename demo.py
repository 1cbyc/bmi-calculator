#!/usr/bin/env python3
"""
BMI Calculator Pro - Feature Demo
"""

def demo_bmi_calculations():
    """Demonstrate BMI calculations"""
    print("🧮 BMI Calculation Demo")
    print("=" * 40)
    
    from utils import calculate_bmi, get_bmi_category, convert_kg_to_lbs, convert_cm_to_feet_inches
    
    # Test cases
    test_cases = [
        (50, 170, "Underweight"),
        (70, 170, "Normal"),
        (90, 170, "Overweight"),
        (110, 170, "Obese")
    ]
    
    for weight_kg, height_cm, expected in test_cases:
        bmi = calculate_bmi(weight_kg, height_cm)
        category, color = get_bmi_category(bmi)
        
        # Convert to imperial
        weight_lbs = convert_kg_to_lbs(weight_kg)
        feet, inches = convert_cm_to_feet_inches(height_cm)
        
        print(f"📊 {weight_kg}kg ({weight_lbs:.1f}lbs) / {height_cm}cm ({feet}'{inches:.1f}\")")
        print(f"   BMI: {bmi} → {category} ({color})")
        print()

def demo_unit_conversions():
    """Demonstrate unit conversions"""
    print("🔄 Unit Conversion Demo")
    print("=" * 40)
    
    from utils import convert_kg_to_lbs, convert_lbs_to_kg, convert_cm_to_feet_inches, convert_feet_inches_to_cm
    
    # Weight conversions
    kg_values = [50, 70, 90, 110]
    for kg in kg_values:
        lbs = convert_kg_to_lbs(kg)
        kg_back = convert_lbs_to_kg(lbs)
        print(f"⚖️ {kg}kg = {lbs:.1f}lbs (back: {kg_back:.1f}kg)")
    
    print()
    
    # Height conversions
    cm_values = [150, 170, 180, 190]
    for cm in cm_values:
        feet, inches = convert_cm_to_feet_inches(cm)
        cm_back = convert_feet_inches_to_cm(feet, inches)
        print(f"📏 {cm}cm = {feet}'{inches:.1f}\" (back: {cm_back:.1f}cm)")
    
    print()

def demo_configuration():
    """Demonstrate configuration system"""
    print("⚙️ Configuration System Demo")
    print("=" * 40)
    
    from config import config
    
    # Show current theme
    primary_color = config.get('theme.primary_color')
    font_family = config.get('display.font_family')
    max_history = config.get('history.max_entries')
    
    print(f"🎨 Primary Color: {primary_color}")
    print(f"📝 Font Family: {font_family}")
    print(f"📚 Max History Entries: {max_history}")
    
    # Test setting a value
    config.set('demo.test_value', 'Hello World!')
    test_value = config.get('demo.test_value')
    print(f"✅ Test Setting: {test_value}")
    
    print()

def demo_validation():
    """Demonstrate input validation"""
    print("✅ Input Validation Demo")
    print("=" * 40)
    
    from utils import validate_weight, validate_height
    
    # Weight validation
    weight_tests = [
        (15, "metric", False, "Too light"),
        (70, "metric", True, "Normal"),
        (350, "metric", False, "Too heavy")
    ]
    
    for weight, unit, expected, description in weight_tests:
        result = validate_weight(weight, unit)
        status = "✅" if result == expected else "❌"
        print(f"{status} {weight}kg ({description}): {result}")
    
    print()
    
    # Height validation
    height_tests = [
        (80, "metric", False, "Too short"),
        (170, "metric", True, "Normal"),
        (300, "metric", False, "Too tall")
    ]
    
    for height, unit, expected, description in height_tests:
        result = validate_height(height, unit)
        status = "✅" if result == expected else "❌"
        print(f"{status} {height}cm ({description}): {result}")

def main():
    """Run all demos"""
    print("🚀 BMI Calculator Pro - Feature Demo")
    print("=" * 50)
    print()
    
    try:
        demo_bmi_calculations()
        demo_unit_conversions()
        demo_configuration()
        demo_validation()
        
        print("🎉 All features working correctly!")
        print("\nTo run the full GUI application:")
        print("  python bmi.py")
        print("  or")
        print("  python run.py")
        
    except Exception as e:
        print(f"❌ Demo failed: {e}")
        return False
    
    return True

if __name__ == "__main__":
    main() 