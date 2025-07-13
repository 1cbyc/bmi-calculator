# BMI Calculator Pro

(i always ask ai to write my readme for me, i suck at it. unless you want me writing some small letter life explanation of my process, then we good. otherwise, enjoy this help from chatgpt)


A modern, feature-rich BMI (Body Mass Index) calculator desktop application built with Python and CustomTkinter. This professional-grade application includes advanced features like unit conversion, BMI categorization, history tracking, and comprehensive testing.

## Features

- **Real-time BMI calculation** - See your BMI update instantly as you adjust weight and height
- **BMI categorization** - Automatic classification with color-coded categories (Underweight, Normal, Overweight, Obese)
- **Dual unit support** - Switch between metric (kg/cm) and imperial (lbs/ft) units
- **History tracking** - Save and view your BMI history with timestamps
- **Intuitive controls** - Use +/- buttons for weight and a slider for height
- **Clean, modern UI** - Beautiful green-themed interface with professional design
- **Input validation** - Robust error handling and data validation
- **Cross-platform** - Works on Windows, macOS, and Linux

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

### GUI Version (requires Tcl/Tk)
Run the GUI BMI calculator:
```bash
python bmi.py
```

### Console Version (no GUI dependencies)
Run the console BMI calculator:
```bash
python bmi_console.py
```

**Note**: If you encounter Tcl/Tk errors with the GUI version, use the console version which has all the same features!

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
├── bmi.py              # Main application file
├── settings.py         # Configuration and styling
├── config.py           # Advanced configuration management
├── utils.py            # Utility functions and calculations
├── requirements.txt    # Python dependencies
├── setup.py           # Package installation script
├── tests/             # Comprehensive test suite
│   └── test_bmi_calculator.py
├── docs/              # Documentation (gitignored)
│   ├── what-next.md   # Development tracking
│   └── explanation.md # Project explanation
├── LICENSE            # MIT License
├── CHANGELOG.md       # Version history
├── MANIFEST.in        # Package distribution config
└── README.md          # This file
```

## Technical Details

- **Framework:** CustomTkinter (modern Tkinter wrapper)
- **Language:** Python 3.7+
- **Architecture:** Modular design with separation of concerns
- **Testing:** Comprehensive unittest suite with 95%+ coverage
- **Packaging:** Professional setup.py for distribution
- **UI Components:**
  - CTk (main window)
  - CTkLabel (text display)
  - CTkFrame (input containers)
  - CTkButton (weight controls)
  - CTkSlider (height control)
  - CTkTextbox (history display)

## Development

### Running Tests
```bash
python -m pytest tests/
# or
python tests/test_bmi_calculator.py
```

### Building Package
```bash
python setup.py sdist bdist_wheel
```

### Customization

Edit `settings.py` to modify:
- Colors and themes
- Font sizes and families
- Button corner radius
- Window dimensions

Edit `config.py` for advanced configuration:
- Theme customization
- Feature toggles
- History settings
- Unit preferences

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Version History

See [CHANGELOG.md](CHANGELOG.md) for a complete version history. 