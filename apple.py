import tkinter as tk
from tkinter import messagebox
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Dummy Dataset for Multi-Sensor Data
# Features: [R, G, B, Firmness, Chemical Index, VOC Level]
data = [
    [200, 50, 30, 85, 0.1, 0.05, 0],  # Grade A: Natural
    [180, 40, 35, 80, 0.2, 0.07, 0],  # Grade A: Natural
    [150, 30, 20, 60, 0.5, 0.2, 1],   # Grade B: Slightly Treated
    [120, 25, 15, 50, 0.8, 0.3, 1],   # Grade B: Moderate Quality
    [100, 60, 50, 40, 1.2, 0.5, 2],   # Grade C: Chemically Treated
    [80, 70, 60, 30, 1.5, 0.7, 2],    # Grade C: Chemically Treated
]

# Splitting Features and Labels
X = np.array([row[:6] for row in data])  # Features
y = np.array([row[6] for row in data])   # Labels

# Train ML Model
model = RandomForestClassifier()
model.fit(X, y)

# Function to Classify Apple Quality
def classify_apple():
    try:
        # Get Inputs from GUI
        r = int(r_input.get())
        g = int(g_input.get())
        b = int(b_input.get())
        firmness = int(firmness_input.get())
        chemical = float(chemical_input.get())
        voc = float(voc_input.get())
        
        # Validate Input Ranges
        if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
            raise ValueError("RGB values should be between 0 and 255.")
        if not (0 <= firmness <= 100):
            raise ValueError("Firmness should be between 0 and 100.")
        if not (0.0 <= chemical <= 2.0):
            raise ValueError("Chemical Index should be between 0.0 and 2.0.")
        if not (0.0 <= voc <= 1.0):
            raise ValueError("VOC Level should be between 0.0 and 1.0.")

        # Predict Quality
        prediction = model.predict([[r, g, b, firmness, chemical, voc]])[0]
        grades = {0: "Grade A: High Quality", 1: "Grade B: Moderate Quality", 2: "Grade C: Low Quality"}
        result = grades[prediction]
        messagebox.showinfo("Result", f"Apple Quality: {result}")
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

# GUI Design
app = tk.Tk()
app.title("Multi-Sensor Apple Quality Classifier")

# Labels and Inputs
tk.Label(app, text="Enter Sensor Data for Apple Quality", font=("Arial", 14)).pack(pady=10)

tk.Label(app, text="Red (0-255):").pack()
r_input = tk.Entry(app)
r_input.pack()

tk.Label(app, text="Green (0-255):").pack()
g_input = tk.Entry(app)
g_input.pack()

tk.Label(app, text="Blue (0-255):").pack()
b_input = tk.Entry(app)
b_input.pack()

tk.Label(app, text="Firmness (0-100):").pack()
firmness_input = tk.Entry(app)
firmness_input.pack()

tk.Label(app, text="Chemical Index (0.0-2.0):").pack()
chemical_input = tk.Entry(app)
chemical_input.pack()

tk.Label(app, text="VOC Level (0.0-1.0):").pack()
voc_input = tk.Entry(app)
voc_input.pack()

tk.Button(app, text="Classify", command=classify_apple, bg="green", fg="white").pack(pady=10)

app.mainloop()

