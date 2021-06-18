from move import AbstractMove

class plaquage  (AbstractMove):
   def __init__(self):
       super.__init__("Plaquage","NORMAL","PHYSICAL","Le lanceur se laisse tombre sur l'ennemie de tout son poids. 30% de chance d'infliger la paralysie.",85.0,1,00,15,0)
   def use(self):
      pass