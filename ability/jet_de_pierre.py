from move import AbstractMove

class jet_de_pierre (AbstractMove):
   def __init__(self):
       super.__init__("Jet de pierre","ROCK","PHYSICAL ","Une pierre tombe sur l'ennemie.",50.0,0,90,15,0)
   def use(self):
      pass