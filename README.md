# BMI Calculator

A modern, user-friendly BMI (Body Mass Index) calculator built with Python and CustomTkinter.

## Features

- **Real-time BMI calculation** - See your BMI update instantly as you adjust weight and height
- **Intuitive controls** - Use +/- buttons for weight and a slider for height
- **Clean, modern UI** - Beautiful green-themed interface
- **Metric units** - Height in meters, weight in kilograms
- **Responsive design** - Fixed window size with proper layout

## Screenshots

The calculator features:
- Large BMI display at the top
- Weight input with large and small increment buttons
- Height slider with meter display
- Unit indicator (metric)

## Installation

1. **Clone or download this project**
2. **Install Python** (3.7 or higher)
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the BMI calculator:
```bash
python bmi.py
```

### How to use:
1. **Adjust weight** using the +/- buttons:
   - Large buttons: ±1 kg
   - Small buttons: ±0.1 kg
2. **Adjust height** using the slider (100-250 cm)
3. **View your BMI** displayed prominently at the top
4. **BMI interpretation:**
   - Underweight: < 18.5
   - Normal: 18.5 - 24.9
   - Overweight: 25 - 29.9
   - Obese: ≥ 30

## Project Structure

```
bmi-calculator/
├── bmi.py          # Main application file
├── settings.py     # Configuration and styling
├── requirements.txt # Python dependencies
└── README.md       # This file
```

## Technical Details

- **Framework:** CustomTkinter (modern Tkinter wrapper)
- **Language:** Python 3.7+
- **UI Components:**
  - CTk (main window)
  - CTkLabel (text display)
  - CTkFrame (input containers)
  - CTkButton (weight controls)
  - CTkSlider (height control)

## Customization

Edit `settings.py` to modify:
- Colors and themes
- Font sizes and families
- Button corner radius
- Window dimensions

## License

This project is open source and available under the MIT License. 