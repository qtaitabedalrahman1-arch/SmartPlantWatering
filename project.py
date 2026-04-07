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



   def train(self,soil_moisture,last_watered,plant_type)   


























