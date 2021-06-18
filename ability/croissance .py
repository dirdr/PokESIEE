from move import AbstractMove

class croissance  (AbstractMove):
   def __init__(self):
       super.__init__("Croissance ","GRASS","STATUS","Le corps du lanceur se developpe pour augmenter attaque et attaque spe d'un cran.",0.0,1,00,20,0)
   def use(self):
      pass