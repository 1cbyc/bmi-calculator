"""
Test suite for BMI Calculator Pro
"""

import unittest
import sys
import os

# Add parent directory to path to import modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import (
    calculate_bmi, get_bmi_category, convert_kg_to_lbs, convert_lbs_to_kg,
    convert_cm_to_feet_inches, convert_feet_inches_to_cm,
    validate_weight, validate_height, format_height_display, format_weight_display
)

class TestBMICalculations(unittest.TestCase):
    """Test BMI calculation functions"""
    
    def test_calculate_bmi_normal(self):
        """Test normal BMI calculation"""
        bmi = calculate_bmi(70, 170)
        self.assertAlmostEqual(bmi, 24.22, places=2)
    
    def test_calculate_bmi_underweight(self):
        """Test underweight BMI calculation"""
        bmi = calculate_bmi(50, 170)
        self.assertAlmostEqual(bmi, 17.30, places=2)
    
    def test_calculate_bmi_overweight(self):
        """Test overweight BMI calculation"""
        bmi = calculate_bmi(90, 170)
        self.assertAlmostEqual(bmi, 31.14, places=2)
    
    def test_calculate_bmi_zero_height(self):
        """Test BMI calculation with zero height"""
        with self.assertRaises(ValueError):
            calculate_bmi(70, 0)
    
    def test_calculate_bmi_negative_height(self):
        """Test BMI calculation with negative height"""
        with self.assertRaises(ValueError):
            calculate_bmi(70, -170)

class TestBMICategories(unittest.TestCase):
    """Test BMI category classification"""
    
    def test_underweight_category(self):
        """Test underweight category"""
        category, color = get_bmi_category(17.5)
        self.assertEqual(category, "Underweight")
        self.assertEqual(color, "#4A90E2")
    
    def test_normal_category(self):
        """Test normal category"""
        category, color = get_bmi_category(22.5)
        self.assertEqual(category, "Normal")
        self.assertEqual(color, "#7ED321")
    
    def test_overweight_category(self):
        """Test overweight category"""
        category, color = get_bmi_category(27.5)
        self.assertEqual(category, "Overweight")
        self.assertEqual(color, "#F5A623")
    
    def test_obese_category(self):
        """Test obese category"""
        category, color = get_bmi_category(32.5)
        self.assertEqual(category, "Obese")
        self.assertEqual(color, "#D0021B")

class TestUnitConversions(unittest.TestCase):
    """Test unit conversion functions"""
    
    def test_kg_to_lbs(self):
        """Test kilogram to pound conversion"""
        lbs = convert_kg_to_lbs(70)
        self.assertAlmostEqual(lbs, 154.32, places=2)
    
    def test_lbs_to_kg(self):
        """Test pound to kilogram conversion"""
        kg = convert_lbs_to_kg(154.32)
        self.assertAlmostEqual(kg, 70, places=2)
    
    def test_cm_to_feet_inches(self):
        """Test centimeter to feet/inches conversion"""
        feet, inches = convert_cm_to_feet_inches(170)
        self.assertEqual(feet, 5)
        self.assertAlmostEqual(inches, 6.93, places=2)
    
    def test_feet_inches_to_cm(self):
        """Test feet/inches to centimeter conversion"""
        cm = convert_feet_inches_to_cm(5, 6.93)
        self.assertAlmostEqual(cm, 170, places=1)

class TestValidation(unittest.TestCase):
    """Test input validation functions"""
    
    def test_validate_weight_metric_valid(self):
        """Test valid metric weight"""
        self.assertTrue(validate_weight(70, "metric"))
    
    def test_validate_weight_metric_invalid_low(self):
        """Test invalid low metric weight"""
        self.assertFalse(validate_weight(15, "metric"))
    
    def test_validate_weight_metric_invalid_high(self):
        """Test invalid high metric weight"""
        self.assertFalse(validate_weight(350, "metric"))
    
    def test_validate_height_metric_valid(self):
        """Test valid metric height"""
        self.assertTrue(validate_height(170, "metric"))
    
    def test_validate_height_metric_invalid_low(self):
        """Test invalid low metric height"""
        self.assertFalse(validate_height(80, "metric"))
    
    def test_validate_height_metric_invalid_high(self):
        """Test invalid high metric height"""
        self.assertFalse(validate_height(300, "metric"))

class TestFormatting(unittest.TestCase):
    """Test display formatting functions"""
    
    def test_format_height_display_metric(self):
        """Test metric height formatting"""
        display = format_height_display(170, "metric")
        self.assertEqual(display, "1.70m")
    
    def test_format_height_display_imperial(self):
        """Test imperial height formatting"""
        display = format_height_display(170, "imperial")
        self.assertEqual(display, "5'6.9\"")
    
    def test_format_weight_display_metric(self):
        """Test metric weight formatting"""
        display = format_weight_display(70, "metric")
        self.assertEqual(display, "70.0kg")
    
    def test_format_weight_display_imperial(self):
        """Test imperial weight formatting"""
        display = format_weight_display(70, "imperial")
        self.assertEqual(display, "154.3lbs")

class TestIntegration(unittest.TestCase):
    """Test integration scenarios"""
    
    def test_full_bmi_workflow(self):
        """Test complete BMI calculation workflow"""
        # Input values
        weight_kg = 70
        height_cm = 170
        
        # Calculate BMI
        bmi = calculate_bmi(weight_kg, height_cm)
        
        # Get category
        category, color = get_bmi_category(bmi)
        
        # Validate inputs
        weight_valid = validate_weight(weight_kg, "metric")
        height_valid = validate_height(height_cm, "metric")
        
        # Format displays
        weight_display = format_weight_display(weight_kg, "metric")
        height_display = format_height_display(height_cm, "metric")
        
        # Assertions
        self.assertAlmostEqual(bmi, 24.22, places=2)
        self.assertEqual(category, "Normal")
        self.assertTrue(weight_valid)
        self.assertTrue(height_valid)
        self.assertEqual(weight_display, "70.0kg")
        self.assertEqual(height_display, "1.70m")

if __name__ == '__main__':
    # Create tests directory if it doesn't exist
    os.makedirs('tests', exist_ok=True)
    
    # Run tests
    unittest.main(verbosity=2) 