from move import AbstractMove

class lance_flamme (AbstractMove):
   def __init__(self):
       super.__init__("Lance-flamme","FIRE","SPECIAL","Le lanceur deferle un torrent de flamme sur l'ennemie. 10% de chance d'infliger la brulure.",90.0,1,00,15,0)
   def use(self):
      pass