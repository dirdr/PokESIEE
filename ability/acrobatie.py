from move import AbstractMove

class acrobatie (AbstractMove):
   def __init__(self):
       super.__init__("Acrobatie","FLYING","PHYSICAL","Le lanceur virevolt dans les airs en frappant l'ennemie. Si celui si a une vitesse plus grande que l'ennemie les degats sont doubles.",65.0,1,00,20,0)
   def use(self):
      pass