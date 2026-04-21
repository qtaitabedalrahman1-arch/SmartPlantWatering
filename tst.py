import tkinter as tk
from tkinter import ttk, messagebox
import random
import math
import matplotlib.pyplot as plt
from project import Plant, Perceptron, Semulated_Annealing, load_all_data

class GardenGUI:
    def __init__(self, root, plants_for_garden, perceptron):
        self.root = root
        self.root.title("Smart Irrigation System | AI & SA Visualization")
        self.root.geometry("1000x700")
        
        self.all_plants = plants_for_garden
        self.perceptron = perceptron
        self.selected_plants = []
        
        self.setup_ui()

    def setup_ui(self):
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.sidebar = ttk.LabelFrame(self.main_frame, text=" النباتات المختارة للـ SA ")
        self.sidebar.pack(side="right", fill="y", padx=5)

        self.plant_listbox = tk.Listbox(self.sidebar, width=35, height=25, font=("Courier", 9))
        self.plant_listbox.pack(pady=5, padx=5)

        ttk.Button(self.sidebar, text="مسح القائمة", command=self.clear_selection).pack(fill="x", pady=5)

        self.canvas_frame = ttk.Frame(self.main_frame)
        self.canvas_frame.pack(side="left", fill="both", expand=True)

        self.canvas = tk.Canvas(self.canvas_frame, width=700, height=550, bg="#ffffff", highlightthickness=2)
        self.canvas.pack(pady=5)
        
        self.canvas.bind("<Button-1>", self.on_click_select)
        self.canvas.bind("<Button-3>", self.add_new_plant)

        self.controls = ttk.Frame(self.root)
        self.controls.pack(side="bottom", fill="x", pady=10)

        ttk.Button(self.controls, text="1. تحليل الذكاء الاصطناعي (Train)", command=self.run_train).pack(side="left", padx=20)
        ttk.Button(self.controls, text="2. تحسين المسار (SA Optimizer)", command=self.run_sa).pack(side="left", padx=20)

        self.status_lbl = ttk.Label(self.root, text="يسار: اختيار | يمين: زراعة نبتة جديدة", foreground="blue", font=("Arial", 10, "bold"))
        self.status_lbl.pack()

        self.draw_all_plants()

    def draw_all_plants(self):
        self.canvas.delete("plant")
        for p in self.all_plants:
            self.draw_single_plant(p)

    def draw_single_plant(self, p):
        tag = f"plant_{id(p)}"
        self.canvas.create_oval(p.x-8, p.y-8, p.x+8, p.y+8, fill="#A9A9A9", tags=("plant", tag))

    def on_click_select(self, event):
        for p in self.all_plants:
            dist = math.sqrt((p.x - event.x)**2 + (p.y - event.y)**2)
            if dist < 15:
                tag_text = f"info_{id(p)}"
                if p not in self.selected_plants:
                    
                    self.selected_plants.append(p)
                    self.canvas.itemconfig(f"plant_{id(p)}", outline="#FFD700", width=3) 
                    
                   
                    info = f"M:{p.soil_moisture}%|H:{p.last_watered}h"
                    self.canvas.create_text(p.x, p.y - 22, text=info, fill="black", 
                                            font=("Arial", 8, "bold"), tags=("info", tag_text))
                else:
                   
                    self.selected_plants.remove(p)
                    self.canvas.itemconfig(f"plant_{id(p)}", outline="", width=1)
                    self.canvas.delete(tag_text)
                
                self.update_listbox()
                break

    def add_new_plant(self, event):
        
        new_p = Plant(random.randint(10, 95), random.randint(1, 48), random.randint(0, 2), event.x, event.y)
        self.all_plants.append(new_p)
        self.draw_single_plant(new_p)
        self.status_lbl.config(text=f"تم زراعة نبتة في الموقع: ({event.x}, {event.y})")

    def update_listbox(self):
        self.plant_listbox.delete(0, tk.END)
        for i, p in enumerate(self.selected_plants):
            self.plant_listbox.insert(tk.END, f"{i+1}: Pos({p.x},{p.y}) | M:{p.soil_moisture}%")

    def clear_selection(self):
        self.selected_plants = []
        self.update_listbox()
        self.canvas.delete("info")
        self.canvas.delete("line")
        for p in self.all_plants:
            self.canvas.itemconfig(f"plant_{id(p)}", outline="", width=1)

    def run_train(self):
        try:
           
            full_data, _ = load_all_data(r"C:\Users\hp\OneDrive\Desktop\Data (1).xlsx")
            self.perceptron.train(full_data)
            
            for p in self.all_plants:
                pred = self.perceptron.evaluat(p.get_plant_features())
                color = "#FF4500" if pred == 1 else "#1E90FF" 
                self.canvas.itemconfig(f"plant_{id(p)}", fill=color)
            
            self.status_lbl.config(text="تم التحليل: الأحمر يحتاج سقاية | الأزرق حالته جيدة", foreground="green")
        except Exception as e:
            messagebox.showerror("خطأ", f"فشل التدريب: {e}")

    def run_sa(self):
        if len(self.selected_plants) < 2: return
        
        sa_engine = Semulated_Annealing(self.all_plants, self.perceptron, self.selected_plants)
        
        best_path, h_temp, h_cost = sa_engine.optimize()
        
        
        self.canvas.delete("line")
        for i in range(len(best_path)-1):
            p1, p2 = best_path[i], best_path[i+1]
            self.canvas.create_line(p1.x, p1.y, p2.x, p2.y, fill="#2E8B57", width=2, tags="line")

        
        plt.figure("SA Real-time Analysis", figsize=(10, 5))
        
        
        plt.subplot(1, 2, 1)
        plt.plot(h_temp, color='orange')
        plt.title("Temperature (with Reheating)")
        plt.grid(True)

        
        plt.subplot(1, 2, 2)
        plt.plot(h_cost, color='blue')
        plt.title("Cost Function (Path Efficiency)")
        plt.grid(True)

        plt.tight_layout()
        plt.show(block=False)

    def plot_temp_decay(self):
      
        temps = []
        t = 100
        for _ in range(500):
            temps.append(t)
            t *= 0.95 
        
        plt.figure("Simulated Annealing - Cooling Schedule")
        plt.plot(temps, color='orange', label='Temperature (T)')
        plt.title("Temperature Decay over Iterations")
        plt.xlabel("Iteration")
        plt.ylabel("Temperature")
        plt.grid(True, linestyle='--')
        plt.legend()
        plt.show(block=False)

