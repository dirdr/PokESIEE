from move import AbstractMove

class rugissement (AbstractMove):
   def __init__(self):
       super.__init__("Rugissement","NORMAL","STATUS","Le lanceur rugit avec son cri sur l'ennemi ce qui baisse son attaque d'un cran ",0.0,1,00,40,0)
   def use(self):
      pass