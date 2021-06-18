from move import AbstractMove

class surpuissance  (AbstractMove):
   def __init__(self):
       super.__init__("Surpuissance ","FIGHTING","PHYSICAL","Une puissante attaque mais qui baisse la defense et defense spe du lanceur.",120.0,1,00,5,0)
   def use(self):
      pass