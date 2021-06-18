from move import AbstractMove

class bomb_beurk (AbstractMove):
   def __init__(self):
       super.__init__("Bomb-beurk","POISON","SPECIAL","Des détritues toxics sont projetes sur l'ennemie. 30% de chance d'empoisonner.",90.0,1,00,10,0)
   def use(self):
      pass