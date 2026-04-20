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
   
def load_dataset_from_excel(file_path):
    df = pd.read_excel(file_path)

    dataset = []

    for _, row in df.iterrows():
        features = [
            row['soil_moisture'] / 100,
            row['last_watered'] / 48,
            row['plant_type'] / 2
        ]

        label = row['needs_water']

        dataset.append((features, label))

    return dataset
    





class Semulated_Annealing:
   def __init__(self, all_plants, perceptron, initial_selection):
      self.all_plants = all_plants  # الـ 20 نبتة كاملة
      self.perceptron = perceptron
      self.current_7 = list(initial_selection)##############؟؟؟؟
      self._tempr=100
      self._coling_rate=0.89


   def calculate_cost(self, current_sequence, w_p, w_d):
        penalty = 0
        total_distance = 0
    
    # --- الجزء الأول: حساب العقوبات (Penalties) بناءً على البيرسبترون ---
    # بنلف على كل النباتات الموجودة في الحديقة (الـ 20 نبتة)
        for plant in self.all_plants:
        # بنستخدم البيرسبترون عشان نتوقع هل النبتة محتاجة مي
        # افترضت إن عندك فنكشن اسمه evaluate بيرجع 0 أو 1
            prediction = self.perceptron.evaluat(plant.get_plant_features())
        
            is_in_sequence = plant in current_sequence
        
        # 1. حالة الـ Missed: النبتة عطشانة بس مش موجودة في المسار
            if prediction == 1 and not is_in_sequence:
                penalty += 1
            
        # 2. حالة الـ Extra: النبتة مش عطشانة بس إنت حاططها في المسار (عقوبة زيادة)
            elif prediction == 0 and is_in_sequence:
                penalty += 1

    # --- الجزء الثاني: حساب المسافة الإجمالية للمسار (Total Distance) ---
    # بنحسب المسافة فقط بين النباتات اللي اخترناهم في current_sequence
        if len(current_sequence) > 1:
           for i in range(len(current_sequence) - 1):
               p1 = current_sequence[i]
               p2 = current_sequence[i+1]
            
            # قانون المسافة الإقليدية (Euclidean Distance)
               dist = math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)
               total_distance += dist

    # --- النتيجة النهائية: الكوست الموزون ---
        weighted_cost = (w_p * penalty) + (w_d * total_distance)
    
        return weighted_cost
        
        
   def  random_succer(self,current_sequence):
        # هون بتحسب (المسافات + النباتات الليsfd نسيناها + الزيادة)
        
        pass   

   def optimize(self,):
        xcurr=self.planrtd
        xbest=xcurr
        while 1:
            tc=self._tempr*self._coling_rate
            xnext=self.random_succer(self.planet)
            current_cost = self.calculate_cost(xcurr)
            next_cost = self.calculate_cost(xnext)
            best_cost = self.calculate_cost(xbest)



            dalta_e=current_cost-next_cost
            if dalta_e>0 :
                xcurr=xnext
                if ((best_cost-current_cost)<0):xbest=xcurr


            e = math.exp(-dalta_e / self._tempr)
            if e > random.random():
                xcurr = xnext    















if __name__ == "__main__":
    my_perceptron = Perceptron()

    try:
        my_data = load_dataset_from_excel(r"C:\Users\hp\OneDrive\Desktop\Data (1).xlsx")
        
        # 3. التدريب
        my_perceptron.train(my_data)

        test_plant = [0.2, 0.8, 0.5] 
        prediction = my_perceptron.evaluat(test_plant)
        
        print(f"النتيجة للنبتة التجريبية: {prediction}")
        
    except FileNotFoundError:
        print("ملف الإكسل مش موجود! تأكد من المسار.")












      






































