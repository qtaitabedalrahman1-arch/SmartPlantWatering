import random
import pandas as pd
import math


class Plant :
    def __init__(self,soil_moisture,last_watered,plant_type,x=0, y=0):
        if 0<= soil_moisture <=100:
          self.soil_moisture=soil_moisture 
        else:
           print("invaled value")
           self.soil_moisture=0
        
        
        if 0<= last_watered <=48:
          self.last_watered=last_watered 
        else:
           print("invaled value")
           self.last_watered=0

        if 0<= plant_type<=2:
           self.plant_type=plant_type
        

        else:
           print("invaled value")
           self.plant_type=0

        self.x = x  
        self.y = y  
  
    def get_plant_features (self):
     return [self.soil_moisture/100,self.last_watered/48,self.plant_type/2]
          



class Perceptron:
   def __init__(self):
      self._weights=[random.uniform(-0.5,0.5) for _ in range(3)]

      self._threshold=0
      self._alfa=0.01

   def activation(self,big_x):
      return 1 if big_x>=0 else 0




   def train(self, dataset):
        iteration = 0
        while iteration < 100:
            total_error = 0
            for inputs, desired_output in dataset:
                big_x= inputs[0] * self._weights[0] + inputs[1] * self._weights[1] + inputs[2] * self._weights[2] +self._threshold
                actual_output = self.activation(big_x)
                error = desired_output - actual_output
                
                delta_w = []
                for i in range(3):
                    temp = inputs[i] * error * self._alfa
                    delta_w.append(temp)
                
                new_w = []
                for i in range(3):
                    tempr = self._weights[i] + delta_w[i]
                    new_w.append(tempr)
                self._weights = new_w   

                total_error += abs(error)

            
            print(f"الدورة رقم {iteration}: مجموع الأخطاء في الـ 100 صف = {total_error}")
            
            if total_error == 0:
                break

            iteration += 1

   def evaluat(self,input): 
      bige_x= input[0] * self._weights[0] + input[1] * self._weights[1] + input[2] * self._weights[2] +self._threshold
      return self.activation(bige_x)
   


def load_all_data(file_path):
    df = pd.read_excel(file_path)

    full_dataset = []
    for _, row in df.iterrows():
        features = [row['soil_moisture']/100, row['last_watered']/48, row['plant_type']/2]
        label = row['needs_water']
        full_dataset.append((features, label))

    last_30_df = df.tail(30)
    garden_plants = []
    for _, row in last_30_df.iterrows():
        new_plant = Plant(
            soil_moisture=row['soil_moisture'],
            last_watered=row['last_watered'],
            plant_type=row['plant_type'],
            x=random.randint(50, 550), 
            y=random.randint(50, 350)
        )
        garden_plants.append(new_plant)

    return full_dataset, garden_plants




class Semulated_Annealing:
   def __init__(self, all_plants, perceptron, initial_selection):
      self.all_plants = all_plants 
      self.perceptron = perceptron
      self.current_selection = list(initial_selection)
      self.remaining_plants = [p for p in all_plants if p not in self.current_selection]
      self._tempr=100
      self._cooling_rate=0.95


   def calculate_cost(self,sequence, w_p, w_d):
        penalty = 0
        total_distance = 0
        current_set = set(sequence)
   
        for plant in self.all_plants:
        
            prediction = self.perceptron.evaluat(plant.get_plant_features())
        
            is_in_sequence = plant in current_set
        
        
            if prediction == 1 and not is_in_sequence:
                penalty += 1
            
            elif prediction == 0 and is_in_sequence:
                penalty += 1

   
        if len(sequence) > 1:
           for i in range(len(sequence) - 1):
               p1 = sequence[i]
               p2 = sequence[i+1]
            
               dist = math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)
               total_distance += dist

        weighted_cost = (w_p * penalty) + (w_d * total_distance)
    
        return weighted_cost
        

   def swap_external(self):
        
        if not self.remaining_plants: return self.current_selection, []
        
        new_sel = list(self.current_selection)
        new_rem = list(self.remaining_plants)
        
        idx_in = random.randint(0, len(new_sel) - 1)
        idx_out = random.randint(0, len(new_rem) - 1)
        
        new_sel[idx_in], new_rem[idx_out] = new_rem[idx_out], new_sel[idx_in]
        return new_sel, new_rem    
   def swap_internal(self):
        if len(self.current_selection) < 2: return self.current_selection, self.remaining_plants
        
        new_sel = list(self.current_selection)
        idx1, idx2 = random.sample(range(len(new_sel)), 2)
        new_sel[idx1], new_sel[idx2] = new_sel[idx2], new_sel[idx1]
        return new_sel, self.remaining_plants

  

   def optimize(self,):
        self.best_selection = list(self.current_selection)
        self.best_cost = self.calculate_cost(self.best_selection, 1000, 1)
        self.best_selection = list(self.current_selection)
        self.best_cost = self.calculate_cost(self.best_selection, 1000, 1)
        self.history_temp = [] 
        self.history_cost = [] 

        
        self._temp = 100
        for _ in range(500):
            new_sel, new_rem = self.swap_external()
            c_cost = self.calculate_cost(self.current_selection, 1000, 1)
            n_cost = self.calculate_cost(new_sel, 1000, 1)
            
            delta_e = n_cost - c_cost

           
            if n_cost < c_cost:
                self.current_selection = list(new_sel)
                self.remaining_plants = list(new_rem)
                
                
                if n_cost < self.best_cost:
                    self.best_cost = n_cost
                    self.best_selection = list(new_sel)

           
            else:
               
                if math.exp(-delta_e / self._temp) > random.random():
                    self.current_selection = list(new_sel)
                    self.remaining_plants = list(new_rem)
                   
            
            self._temp *= self._cooling_rate
            self.history_temp.append(self._temp)
            self.history_cost.append(c_cost)
            self._temp *= self._cooling_rate

            

        return self.best_selection, self.history_temp, self.history_cost















      






































