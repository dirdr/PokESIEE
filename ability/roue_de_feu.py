from move import AbstractMove

class roue_de_feu (AbstractMove):
   def __init__(self):
       super.__init__("Roue de feu","FIRE","PHYSICAL","Le lanceur s'entoure de feu et charge l'ennemie. 10% d'infliger la brulure.",60.0,1,00,25,0)
   def use(self):
      pass