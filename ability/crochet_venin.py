from move import AbstractMove

class crochet_venin (AbstractMove):
   def __init__(self):
       super.__init__("Crochet venin ","POISON","PHYSICAL","Le lanceur mord l'ennemi de ses crocs toxiques. 30% de chance d'empoisonner.",60.0,1,00,15,0)
   def use(self):
      pass