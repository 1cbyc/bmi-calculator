"""
Configuration settings for BMI Calculator Pro
"""

import json
import os
from typing import Dict, Any

class Config:
    def __init__(self, config_file: str = "config.json"):
        self.config_file = config_file
        self.default_config = {
            "theme": {
                "primary_color": "#50BFAB",
                "secondary_color": "#3A8A7B", 
                "background_color": "#F2F2F2",
                "text_color": "#1F1F1F",
                "accent_color": "#7ED321"
            },
            "window": {
                "width": 700,
                "height": 800,
                "resizable": False,
                "center_on_startup": True
            },
            "units": {
                "default": "metric",
                "available": ["metric", "imperial"]
            },
            "history": {
                "max_entries": 100,
                "auto_save": True,
                "show_recent_count": 5
            },
            "display": {
                "font_family": "Calibri",
                "main_text_size": 150,
                "input_font_size": 26,
                "switch_font_size": 18,
                "button_corner_radius": 17
            },
            "features": {
                "show_bmi_category": True,
                "show_history": True,
                "unit_conversion": True,
                "auto_calculate": True
            }
        }
        self.config = self.load_config()
    
    def load_config(self) -> Dict[str, Any]:
        """Load configuration from file or create default"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    return json.load(f)
            else:
                return self.default_config.copy()
        except Exception as e:
            print(f"Error loading config: {e}")
            return self.default_config.copy()
    
    def save_config(self) -> bool:
        """Save current configuration to file"""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving config: {e}")
            return False
    
    def get(self, key: str, default=None):
        """Get configuration value using dot notation (e.g., 'theme.primary_color')"""
        keys = key.split('.')
        value = self.config
        try:
            for k in keys:
                value = value[k]
            return value
        except (KeyError, TypeError):
            return default
    
    def set(self, key: str, value: Any) -> bool:
        """Set configuration value using dot notation"""
        keys = key.split('.')
        config = self.config
        try:
            for k in keys[:-1]:
                if k not in config:
                    config[k] = {}
                config = config[k]
            config[keys[-1]] = value
            return self.save_config()
        except Exception as e:
            print(f"Error setting config: {e}")
            return False
    
    def reset_to_defaults(self) -> bool:
        """Reset configuration to default values"""
        self.config = self.default_config.copy()
        return self.save_config()

# Global configuration instance
config = Config() 