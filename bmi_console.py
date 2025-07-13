"""
BMI Calculator Pro - Console Version
A fully functional BMI calculator that works without GUI dependencies
"""

import sys
import os
from datetime import datetime
import json

# Import our utility functions
from utils import (
    calculate_bmi, get_bmi_category, convert_kg_to_lbs, convert_lbs_to_kg,
    convert_cm_to_feet_inches, convert_feet_inches_to_cm,
    validate_weight, validate_height, create_history_entry
)

class ConsoleBMICalculator:
    def __init__(self):
        self.history = []
        self.unit_mode = "metric"
        self.load_history()
    
    def load_history(self):
        """Load BMI history from file"""
        try:
            if os.path.exists('bmi_history.json'):
                with open('bmi_history.json', 'r') as f:
                    self.history = json.load(f)
        except:
            self.history = []
    
    def save_history(self):
        """Save BMI history to file"""
        try:
            with open('bmi_history.json', 'w') as f:
                json.dump(self.history, f, indent=2)
        except:
            pass
    
    def clear_screen(self):
        """Clear the console screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_banner(self):
        """Display application banner"""
        print("=" * 60)
        print("🚀 BMI Calculator Pro - Console Version")
        print("=" * 60)
        print()
    
    def get_weight(self):
        """Get weight input from user"""
        while True:
            try:
                if self.unit_mode == "metric":
                    weight = float(input("Enter weight (kg): "))
                    if validate_weight(weight, "metric"):
                        return weight
                    else:
                        print("❌ Weight must be between 20-300 kg")
                else:
                    weight_lbs = float(input("Enter weight (lbs): "))
                    if validate_weight(weight_lbs, "imperial"):
                        return convert_lbs_to_kg(weight_lbs)
                    else:
                        print("❌ Weight must be between 44-661 lbs")
            except ValueError:
                print("❌ Please enter a valid number")
    
    def get_height(self):
        """Get height input from user"""
        while True:
            try:
                if self.unit_mode == "metric":
                    height = float(input("Enter height (cm): "))
                    if validate_height(height, "metric"):
                        return height
                    else:
                        print("❌ Height must be between 100-250 cm")
                else:
                    feet = int(input("Enter height (feet): "))
                    inches = float(input("Enter height (inches): "))
                    height_cm = convert_feet_inches_to_cm(feet, inches)
                    if validate_height(height_cm, "metric"):
                        return height_cm
                    else:
                        print("❌ Height must be between 3.3-8.2 feet")
            except ValueError:
                print("❌ Please enter a valid number")
    
    def calculate_and_display(self, weight_kg, height_cm):
        """Calculate and display BMI results"""
        print("\n" + "=" * 40)
        print("📊 BMI CALCULATION RESULTS")
        print("=" * 40)
        
        # Calculate BMI
        bmi = calculate_bmi(weight_kg, height_cm)
        category, color = get_bmi_category(bmi)
        
        # Display in both units
        weight_lbs = convert_kg_to_lbs(weight_kg)
        feet, inches = convert_cm_to_feet_inches(height_cm)
        
        print(f"📏 Height: {height_cm}cm ({feet}'{inches:.1f}\")")
        print(f"⚖️ Weight: {weight_kg:.1f}kg ({weight_lbs:.1f}lbs)")
        print(f"📊 BMI: {bmi}")
        print(f"🏷️ Category: {category}")
        print(f"🎨 Color Code: {color}")
        
        # BMI interpretation
        print("\n📋 BMI Categories:")
        print("• Underweight: < 18.5 (Blue)")
        print("• Normal: 18.5 - 24.9 (Green)")
        print("• Overweight: 25 - 29.9 (Orange)")
        print("• Obese: ≥ 30 (Red)")
        
        return bmi, category
    
    def save_to_history(self, weight_kg, height_cm, bmi, category):
        """Save current calculation to history"""
        entry = create_history_entry(weight_kg, height_cm, bmi, self.unit_mode)
        self.history.append(entry)
        self.save_history()
        print(f"\n✅ Saved to history: {entry['date']}")
    
    def show_history(self):
        """Display BMI history"""
        if not self.history:
            print("\n📚 No history yet. Calculate your first BMI!")
            return
        
        print("\n" + "=" * 40)
        print("📚 BMI HISTORY")
        print("=" * 40)
        
        # Show last 10 entries
        recent = self.history[-10:]
        for i, entry in enumerate(reversed(recent), 1):
            print(f"{i:2d}. {entry['date']}: BMI {entry['bmi']} ({entry['category']})")
            print(f"    Weight: {entry['weight']}kg, Height: {entry['height']}cm")
    
    def toggle_units(self):
        """Toggle between metric and imperial units"""
        self.unit_mode = "imperial" if self.unit_mode == "metric" else "metric"
        print(f"\n🔄 Switched to {self.unit_mode} units")
    
    def show_menu(self):
        """Display main menu"""
        print("\n📋 MAIN MENU")
        print("=" * 20)
        print("1. Calculate BMI")
        print("2. View History")
        print("3. Switch Units (Current: " + self.unit_mode.title() + ")")
        print("4. Clear History")
        print("5. Exit")
        print()
    
    def clear_history(self):
        """Clear BMI history"""
        self.history = []
        self.save_history()
        print("🗑️ History cleared!")
    
    def run(self):
        """Main application loop"""
        while True:
            self.clear_screen()
            self.display_banner()
            self.show_menu()
            
            try:
                choice = input("Enter your choice (1-5): ").strip()
                
                if choice == "1":
                    print("\n🧮 BMI CALCULATOR")
                    print("-" * 20)
                    weight_kg = self.get_weight()
                    height_cm = self.get_height()
                    
                    bmi, category = self.calculate_and_display(weight_kg, height_cm)
                    
                    save = input("\n💾 Save to history? (y/n): ").lower().strip()
                    if save in ['y', 'yes']:
                        self.save_to_history(weight_kg, height_cm, bmi, category)
                    
                    input("\nPress Enter to continue...")
                
                elif choice == "2":
                    self.show_history()
                    input("\nPress Enter to continue...")
                
                elif choice == "3":
                    self.toggle_units()
                    input("Press Enter to continue...")
                
                elif choice == "4":
                    confirm = input("🗑️ Are you sure you want to clear history? (y/n): ").lower().strip()
                    if confirm in ['y', 'yes']:
                        self.clear_history()
                    input("Press Enter to continue...")
                
                elif choice == "5":
                    print("\n👋 Thanks for using BMI Calculator Pro!")
                    break
                
                else:
                    print("❌ Invalid choice. Please enter 1-5.")
                    input("Press Enter to continue...")
                    
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"\n❌ Error: {e}")
                input("Press Enter to continue...")

def main():
    """Start the console BMI calculator"""
    try:
        calculator = ConsoleBMICalculator()
        calculator.run()
    except Exception as e:
        print(f"❌ Application error: {e}")
        input("Press Enter to exit...")

if __name__ == "__main__":
    main() 