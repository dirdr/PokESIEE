from move import AbstractMove

class roc_boulet  (AbstractMove):
   def __init__(self):
       super.__init__("Roc boulet ","ROCK","PHYSICAL ","Le lanceur attaque en projetant un gros rocher sur l'ennemi.",120.0,0,70,5,0)
   def use(self):
      pass