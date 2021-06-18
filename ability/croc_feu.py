from move import AbstractMove

class croc_feu (AbstractMove):
   def __init__(self):
       super.__init__("Croc feu","FIRE","PHYSICAL","Le lanceur embrase ses croc pour modre l'ennemie. 10% de chance d'infliger la brulure.",65.0,0,95,15,0)
   def use(self):
      pass