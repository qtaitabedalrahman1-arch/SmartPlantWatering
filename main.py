from project import * 
from tst import * 
import tkinter as tk


if __name__ == "__main__":
    file_path = r"C:\Users\hp\OneDrive\Desktop\Data (1).xlsx"
    try:
        _, initial_plants = load_all_data(file_path)
        root = tk.Tk()
        brain = Perceptron()
        app = GardenGUI(root, initial_plants, brain)
        root.mainloop()
    except Exception as e:
        print(f"Error starting the app: {e}")