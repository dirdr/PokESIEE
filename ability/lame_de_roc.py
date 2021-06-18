from move import AbstractMove

class lame_de_roc (AbstractMove):
   def __init__(self):
       super.__init__("Lame de roc","ROCK","PHYSICAL","Fait surgir des pierres aiguisées sous l'ennemi.",100.0,0,80,5,0)
   def use(self):
      pass