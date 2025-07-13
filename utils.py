"""
Utility functions for BMI Calculator Pro
"""

import re
from typing import Tuple, Optional, Dict, Any
from datetime import datetime

def calculate_bmi(weight_kg: float, height_cm: float) -> float:
    """
    Calculate BMI given weight in kg and height in cm
    
    Args:
        weight_kg: Weight in kilograms
        height_cm: Height in centimeters
        
    Returns:
        BMI value rounded to 2 decimal places
        
    Raises:
        ValueError: If height is zero or negative
    """
    if height_cm <= 0:
        raise ValueError("Height must be positive")
    
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)

def get_bmi_category(bmi: float) -> Tuple[str, str]:
    """
    Get BMI category and color based on BMI value
    
    Args:
        bmi: BMI value
        
    Returns:
        Tuple of (category_name, color_hex)
    """
    if bmi < 18.5:
        return "Underweight", "#4A90E2"  # Blue
    elif bmi < 25:
        return "Normal", "#7ED321"  # Green
    elif bmi < 30:
        return "Overweight", "#F5A623"  # Orange
    else:
        return "Obese", "#D0021B"  # Red

def convert_kg_to_lbs(kg: float) -> float:
    """Convert kilograms to pounds"""
    return kg * 2.20462

def convert_lbs_to_kg(lbs: float) -> float:
    """Convert pounds to kilograms"""
    return lbs / 2.20462

def convert_cm_to_feet_inches(cm: float) -> Tuple[int, float]:
    """
    Convert centimeters to feet and inches
    
    Returns:
        Tuple of (feet, inches)
    """
    total_inches = cm / 2.54
    feet = int(total_inches // 12)
    inches = total_inches % 12
    return feet, inches

def convert_feet_inches_to_cm(feet: int, inches: float) -> float:
    """Convert feet and inches to centimeters"""
    total_inches = feet * 12 + inches
    return total_inches * 2.54

def validate_weight(weight: float, unit: str = "metric") -> bool:
    """
    Validate weight input
    
    Args:
        weight: Weight value
        unit: Unit of measurement ("metric" or "imperial")
        
    Returns:
        True if valid, False otherwise
    """
    if unit == "metric":
        return 20 <= weight <= 300  # 20-300 kg
    else:
        return 44 <= weight <= 661  # 44-661 lbs

def validate_height(height: float, unit: str = "metric") -> bool:
    """
    Validate height input
    
    Args:
        height: Height value
        unit: Unit of measurement ("metric" or "imperial")
        
    Returns:
        True if valid, False otherwise
    """
    if unit == "metric":
        return 100 <= height <= 250  # 100-250 cm
    else:
        return 3.3 <= height <= 8.2  # 3.3-8.2 feet

def format_height_display(height_cm: float, unit: str = "metric") -> str:
    """
    Format height for display
    
    Args:
        height_cm: Height in centimeters
        unit: Display unit ("metric" or "imperial")
        
    Returns:
        Formatted height string
    """
    if unit == "metric":
        text_string = str(int(height_cm))
        if len(text_string) >= 2:
            meter = text_string[0]
            cm = text_string[1:]
            return f'{meter}.{cm}m'
        else:
            return f'0.{text_string}m'
    else:
        feet, inches = convert_cm_to_feet_inches(height_cm)
        return f"{feet}'{inches:.1f}\""

def format_weight_display(weight_kg: float, unit: str = "metric") -> str:
    """
    Format weight for display
    
    Args:
        weight_kg: Weight in kilograms
        unit: Display unit ("metric" or "imperial")
        
    Returns:
        Formatted weight string
    """
    if unit == "metric":
        return f"{weight_kg:.1f}kg"
    else:
        lbs = convert_kg_to_lbs(weight_kg)
        return f"{lbs:.1f}lbs"

def create_history_entry(weight: float, height: float, bmi: float, unit: str) -> Dict[str, Any]:
    """
    Create a history entry
    
    Args:
        weight: Weight value
        height: Height value
        bmi: Calculated BMI
        unit: Unit system used
        
    Returns:
        History entry dictionary
    """
    return {
        'date': datetime.now().strftime("%Y-%m-%d %H:%M"),
        'weight': weight,
        'height': height,
        'bmi': bmi,
        'unit': unit,
        'category': get_bmi_category(bmi)[0]
    }

def sanitize_filename(filename: str) -> str:
    """
    Sanitize filename for safe file operations
    
    Args:
        filename: Original filename
        
    Returns:
        Sanitized filename
    """
    # Remove or replace invalid characters
    filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
    # Remove leading/trailing spaces and dots
    filename = filename.strip(' .')
    # Ensure it's not empty
    if not filename:
        filename = "bmi_data"
    return filename

def get_app_version() -> str:
    """Get application version"""
    return "1.0.0"

def get_system_info() -> Dict[str, str]:
    """Get system information for debugging"""
    import platform
    import sys
    
    return {
        "python_version": sys.version,
        "platform": platform.platform(),
        "architecture": platform.architecture()[0],
        "processor": platform.processor()
    } 