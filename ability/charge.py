from move import AbstractMove

class charge (AbstractMove):
   def __init__(self):
       super.__init__("Charge","NORMAL","PHYSICAL","le lanceur charge sur l'ennemie.",40.0,1,00,35,0)
   def use(self):
      pass