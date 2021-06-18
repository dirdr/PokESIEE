from move import AbstractMove

class griffe (AbstractMove):
   def __init__(self):
       super.__init__("Griffe ","NORMAL","PHYSICAL","Le lanceur attaque avec ses griffes",40.0,1,00,35,0)
   def use(self):
      pass