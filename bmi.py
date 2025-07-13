import customtkinter as ctk
from settings import *
import json
import os
from datetime import datetime

class App(ctk.CTk):
    def __init__(self):
        # Window Setup 
        super().__init__(fg_color = GREEN)
        self.title('BMI Calculator Pro')
        self.geometry('700x800')
        self.resizable(False, False)

        # Layout Setup 
        self.columnconfigure(0, weight = 1)
        self.rowconfigure((0, 1, 2, 3, 4, 5), weight= 1, uniform = 'a')

        # Data 
        self.height_int = ctk.IntVar( value = 170 )
        self.weight_float = ctk.DoubleVar( value = 65 )
        self.bmi_string = ctk.StringVar()
        self.category_string = ctk.StringVar()
        self.unit_mode = ctk.StringVar(value="metric")  # metric or imperial
        self.history = []
        self.load_history()
        self.update_bmi()
        
        # Setup for Tracing 
        self.height_int.trace('w', self.update_bmi)
        self.weight_float.trace('w', self.update_bmi)

        # Widget Setup 
        ResultText(self, self.bmi_string, self.category_string)
        WeightInput(self, self.weight_float, self.unit_mode)
        HeightInput(self, self.height_int, self.unit_mode)
        UnitSwitcher(self, self.unit_mode, self)
        HistoryPanel(self, self.history, self)
        
        # Center window on screen
        self.center_window()

        self.mainloop()
    
    def center_window(self):
        """Center the window on the screen"""
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')
    
    def update_bmi(self, *args):
        height_meter = self.height_int.get() / 100
        weight_kg = self.weight_float.get()
        if height_meter > 0:  # Prevent division by zero
            bmi_result = round(weight_kg / height_meter ** 2, 2)
            self.bmi_string.set(bmi_result)
            self.update_category(bmi_result)
        else:
            self.bmi_string.set("0.0")
            self.category_string.set("")
    
    def update_category(self, bmi):
        """Update BMI category based on BMI value"""
        if bmi < 18.5:
            category = "Underweight"
            color = "#4A90E2"  # Blue
        elif bmi < 25:
            category = "Normal"
            color = "#7ED321"  # Green
        elif bmi < 30:
            category = "Overweight"
            color = "#F5A623"  # Orange
        else:
            category = "Obese"
            color = "#D0021B"  # Red
        
        self.category_string.set(f"{category} ({color})")
    
    def save_to_history(self):
        """Save current BMI calculation to history"""
        entry = {
            'date': datetime.now().strftime("%Y-%m-%d %H:%M"),
            'weight': self.weight_float.get(),
            'height': self.height_int.get(),
            'bmi': float(self.bmi_string.get()),
            'unit': self.unit_mode.get()
        }
        self.history.append(entry)
        self.save_history()
    
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

class ResultText(ctk.CTkFrame):
    def __init__(self, parent, bmi_string, category_string):
        super().__init__(master=parent, fg_color="transparent")
        self.grid(column=0, row=0, rowspan=2, sticky='nsew', padx=20, pady=20)
        
        # BMI Display
        font_large = ctk.CTkFont(family=FONT, size=MAIN_TEXT_SIZE, weight='bold')
        self.bmi_label = ctk.CTkLabel(self, text="22.5", font=font_large, 
                                     text_color=WHITE, textvariable=bmi_string)
        self.bmi_label.pack(expand=True)
        
        # Category Display
        font_medium = ctk.CTkFont(family=FONT, size=INPUT_FONT_SIZE, weight='bold')
        self.category_label = ctk.CTkLabel(self, text="", font=font_medium,
                                         text_color=WHITE, textvariable=category_string)
        self.category_label.pack(pady=10)

class WeightInput(ctk.CTkFrame):
    def __init__(self, parent, weight_float, unit_mode):
        super().__init__(master=parent, fg_color=WHITE)
        self.grid(column=0, row=2, sticky='nsew', padx=10, pady=10)
        self.weight_float = weight_float
        self.unit_mode = unit_mode

        # Layout for Weight Input
        self.rowconfigure(0, weight=1, uniform='b')
        self.columnconfigure(0, weight=2, uniform='b')
        self.columnconfigure(1, weight=1, uniform='b')
        self.columnconfigure(2, weight=3, uniform='b')
        self.columnconfigure(3, weight=1, uniform='b')
        self.columnconfigure(4, weight=2, uniform='b')

        # Text Setup
        font = ctk.CTkFont(family=FONT, size=INPUT_FONT_SIZE)
        self.label = ctk.CTkLabel(self, text='70kg', text_color=BLACK, font=font)
        self.label.grid(row=0, column=2)
        
        # Update label when unit changes
        self.unit_mode.trace('w', self.update_label)

        # Buttons Setup 
        minus_button = ctk.CTkButton(self, command=lambda: self.update_weight(('minus', 'large')), text='-', 
                                     font=font, text_color=BLACK,
                                      fg_color=LIGHT_GRAY, 
                                      hover_color=GRAY, 
                                      corner_radius=BUTTON_CORNER_RADIUS)
        minus_button.grid(row=0, 
                          column=0, 
                          sticky='ns', 
                          padx=8, pady=8)
        
        plus_button = ctk.CTkButton(self, command=lambda: self.update_weight(('plus', 'large')), text='+', 
                                    font=font, 
                                    text_color=BLACK, 
                                    fg_color=LIGHT_GRAY, 
                                    hover_color=GRAY, 
                                    corner_radius=BUTTON_CORNER_RADIUS)
        plus_button.grid(row=0, 
                         column=4, 
                         sticky='ns', 
                         padx=8, pady=8)

        small_plus_button = ctk.CTkButton(self, command=lambda: self.update_weight(('plus', 'small')), text='+', 
                                          font=font, text_color=BLACK, 
                                          fg_color=LIGHT_GRAY, 
                                          hover_color=GRAY, 
                                          corner_radius=BUTTON_CORNER_RADIUS)
        small_plus_button.grid(row=0, 
                               column=3, 
                               padx=4, pady=4)
        
        small_minus_button = ctk.CTkButton(self, command=lambda: self.update_weight(('minus', 'small')), text='-', 
                                           font=font, 
                                           text_color=BLACK, 
                                           fg_color=LIGHT_GRAY, 
                                           hover_color=GRAY, 
                                           corner_radius=BUTTON_CORNER_RADIUS)
        small_minus_button.grid(row=0, 
                                column=1, 
                                padx=4, pady=4)
        
    def update_weight(self, info=None):
        amount = 1 if info[1] == 'large' else 0.1
        if info[0] == 'plus':
            self.weight_float.set(self.weight_float.get() + amount)
        else:
            self.weight_float.set(self.weight_float.get() - amount)
    
    def update_label(self, *args):
        unit = self.unit_mode.get()
        weight = self.weight_float.get()
        if unit == "metric":
            self.label.configure(text=f"{weight:.1f}kg")
        else:
            lbs = weight * 2.20462
            self.label.configure(text=f"{lbs:.1f}lbs")

class HeightInput(ctk.CTkFrame):
    def __init__(self, parent, height_int, unit_mode):
        super().__init__(master=parent, fg_color=WHITE)
        self.grid(row=3, column=0, sticky='nsew', padx=10, pady=10)
        self.height_int = height_int
        self.unit_mode = unit_mode

        # Widgets Setup 
        self.slider = ctk.CTkSlider(master=self, 
                               command=self.update_text,
                               button_color=GREEN, 
                               button_hover_color=GRAY, 
                               progress_color=GREEN, 
                               fg_color=LIGHT_GRAY,
                               variable=height_int, 
                               from_=100, to=250)
        self.slider.pack(side='left', fill='x', expand=True, padx=10, pady=10)

        self.output_string = ctk.StringVar()
        self.update_text(height_int.get())
        self.unit_mode.trace('w', lambda *args: self.update_text(height_int.get()))

        self.output_text = ctk.CTkLabel(self, textvariable=self.output_string, text='1.80m', text_color=BLACK, 
                                   font=ctk.CTkFont(family=FONT, 
                                                  size=INPUT_FONT_SIZE))
        self.output_text.pack(side='left', padx=10, pady=10)
    
    def update_text(self, amount):
        unit = self.unit_mode.get()
        if unit == "metric":
            # Measurement Conversion 
            text_string = str(int(amount))
            if len(text_string) >= 2:
                meter = text_string[0]
                cm = text_string[1:]
                self.output_string.set(f'{meter}.{cm}m')
            else:
                self.output_string.set(f'0.{text_string}m')
        else:
            # Imperial conversion
            cm = int(amount)
            feet = cm // 30.48
            inches = (cm % 30.48) / 2.54
            self.output_string.set(f"{feet}'{inches:.1f}\"")

class UnitSwitcher(ctk.CTkFrame):
    def __init__(self, parent, unit_mode, app):
        super().__init__(master=parent, fg_color="transparent")
        self.place(relx=0.98, rely=0.01, anchor='ne')
        self.unit_mode = unit_mode
        self.app = app
        
        # Create switch button
        self.switch_button = ctk.CTkButton(
            self, 
            text="Metric", 
            command=self.toggle_unit,
            font=ctk.CTkFont(family=FONT, size=SWITCH_FONT_SIZE, weight='bold'),
            fg_color=DARK_GREEN,
            hover_color=GREEN,
            text_color=WHITE,
            corner_radius=10
        )
        self.switch_button.pack()
        
        # Update button text when unit changes
        self.unit_mode.trace('w', self.update_button_text)
    
    def toggle_unit(self):
        current = self.unit_mode.get()
        if current == "metric":
            self.unit_mode.set("imperial")
        else:
            self.unit_mode.set("metric")
    
    def update_button_text(self, *args):
        unit = self.unit_mode.get()
        self.switch_button.configure(text=unit.title())

class HistoryPanel(ctk.CTkFrame):
    def __init__(self, parent, history, app):
        super().__init__(master=parent, fg_color=WHITE)
        self.grid(row=4, column=0, sticky='nsew', padx=10, pady=10)
        self.history = history
        self.app = app
        
        # Title
        title = ctk.CTkLabel(self, text="BMI History", 
                            font=ctk.CTkFont(family=FONT, size=INPUT_FONT_SIZE, weight='bold'),
                            text_color=BLACK)
        title.pack(pady=5)
        
        # Save button
        save_button = ctk.CTkButton(self, text="Save Current", 
                                   command=self.app.save_to_history,
                                   font=ctk.CTkFont(family=FONT, size=12),
                                   fg_color=GREEN, hover_color=DARK_GREEN,
                                   text_color=WHITE)
        save_button.pack(pady=5)
        
        # History display
        self.history_text = ctk.CTkTextbox(self, height=100, 
                                          font=ctk.CTkFont(family=FONT, size=10))
        self.history_text.pack(fill='both', expand=True, padx=10, pady=5)
        
        self.update_history_display()
    
    def update_history_display(self):
        self.history_text.delete("1.0", "end")
        if not self.history:
            self.history_text.insert("1.0", "No history yet. Save your first BMI!")
            return
        
        # Show last 5 entries
        recent = self.history[-5:]
        for entry in reversed(recent):
            text = f"{entry['date']}: BMI {entry['bmi']} ({entry['weight']}kg, {entry['height']}cm)\n"
            self.history_text.insert("1.0", text)

if __name__ == '__main__':
    App()
    