from move import AbstractMove

class etonnement  (AbstractMove):
   def __init__(self):
       super.__init__("Etonnement ","GHOST","PHYSICAL","Le lanceur attaque l'ennemi en poussant un cri terrifiant.",30.0,1,00,30,0)
   def use(self):
      pass