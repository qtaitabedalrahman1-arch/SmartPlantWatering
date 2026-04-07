#  Smart Plant Watering System

An AI-based system that helps schedule plant watering efficiently using **Machine Learning (Perceptron)** and **Optimization (Simulated Annealing)**.

---

##  Project Overview

This project aims to automate the decision of whether a plant needs watering and optimize the sequence of watering to minimize effort.

The system consists of two main components:

1. **Perceptron Classifier**

   * Predicts whether a plant needs water based on:

     * Soil moisture
     * Last watered time
     * Plant type

2. **Simulated Annealing Optimizer**

   * Finds the most efficient watering order
   * Minimizes:

     * Distance walked
     * Missed plants
     * Unnecessary watering

---

##  Machine Learning Model

The Perceptron model:

* Uses normalized input features
* Learns weights using a simple update rule
* Outputs:

  * `1` → Needs water
  * `0` → Does not need water

---

## 🌿 Plant Features

Each plant is represented by:

| Feature       | Range      |
| ------------- | ---------- |
| Soil Moisture | 0 – 100    |
| Last Watered  | 0 – 48 hrs |
| Plant Type    | 0–2        |

After normalization:

* Soil moisture → /100
* Last watered → /48
* Plant type → /2

---

## ⚙️ Project Structure

```
SmartPlantWatering/
├── plant.py         # Plant class
├── perceptron.py   # Perceptron model
├── main.py         # Training & testing
├── README.md
```

---

##  How to Run

1. Clone the repository:

```bash
git clone https://github.com/qtaitabedalrahman1/SmartPlantWatering.git
cd SmartPlantWatering
```

2. Run the main file:

```bash
python main.py
```

---

##  Example Workflow

1. Create plant objects
2. Extract features
3. Train the perceptron
4. Predict watering decision

---

## Future Improvements

* Add GUI for plant positions
* Implement full Simulated Annealing optimization
* Improve dataset and training accuracy
* Add visualization for learning process

---

##  Key Learning Outcomes

* Understanding Perceptron algorithm
* Applying basic Machine Learning concepts
* Using optimization algorithms (Simulated Annealing)
* Structuring a real-world AI project

---

##  Author

Developed by [Abedalrahman Qtait]

---

## ⭐ Notes

This project is part of an academic assignment and focuses on learning fundamental AI and optimization techniques.
