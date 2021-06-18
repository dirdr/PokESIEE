from move import AbstractMove

class fatal_foudre (AbstractMove):
   def __init__(self):
       super.__init__("Fatal-foudre","ELECTRIC ","SPECIAL","Le lanceur fait s'abbatre la foudre sur l'ennemie. 15% de chance d'infliger la paralysie.",110.0,75,00,10,0)
   def use(self):
      pass