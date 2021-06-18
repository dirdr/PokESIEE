from move import AbstractMove

class croc_givre (AbstractMove):
   def __init__(self):
       super.__init__("Croc givre","ICE","PHYSICAL","Le lanceur utilise une morsure glaciale. 15% de chance de geler.",65.0,0,95,15,0)
   def use(self):
      pass