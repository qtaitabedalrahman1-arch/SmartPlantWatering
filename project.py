import random

class Plant :
    def __init__(self,soil_moisture,last_watered,plant_type):
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
           
  
    def get_plant_features (self):
     return [self.soil_moisture/100,self.last_watered/48,self.plant_type/2]
          



class Perceptron:
   def __init__(self):
      self._weights=[random.uniform(-0.5,0.5) for _ in range(3)]

      self._threshold=1
      self._alfa=0.1

   def activation(self,big_x):
      return 1 if big_x>=0 else 0
   

   def train (self,inputs,desired_output) :
    iteration=0
    error=1
    while error !=0 and iteration < 20:
      big_x= inputs[0] * self._weights[0] + inputs[1] * self._weights[1] + inputs[2] * self._weights[2] +self._threshold

      actual_output = self.activation(big_x)
      error = desired_output-actual_output
      delta_w=[]
      for i in range(3):
       temp = inputs[i] *error* self._alfa
       delta_w.append(temp)
      new_w=[]
      for i in range(3):
         tempr= self._weights[i]+delta_w[i]
         new_w.append(tempr)
      self._weights=new_w   
      iteration +=1

   def evaluat(self,input): 
      bige_x= input[0] * self._weights[0] + input[1] * self._weights[1] + input[2] * self._weights[2] +self._threshold
      return self.activation(bige_x)
   

    














      






































