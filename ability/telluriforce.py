from move import AbstractMove

class telluriforce (AbstractMove):
   def __init__(self):
       super.__init__("Telluriforce ","GROUND","SPECIAL","De terribles seismes secouent l'ennemie. 10% de chance de baisser la defense spe de l'ennemie.",90.0,1,00,10,0)
   def use(self):
      pass