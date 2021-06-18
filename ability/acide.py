from move import AbstractMove

class acide (AbstractMove):
   def __init__(self):
       super.__init__("Acide","POISON","SPECIAL","Le lanceur attaque l'ennemi avec un jet d'acide corrosif. 10% de chance de baiser la defense spe ennemie.",40.0,1,00,30,0)
   def use(self):
      pass