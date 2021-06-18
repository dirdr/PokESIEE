from move import AbstractMove

class griffe_acier (AbstractMove):
   def __init__(self):
       super.__init__("Griffe acier","STEEL","PHYSICAL","Le lanceur durcit ses griffes pour attaquer l'ennemie. 10% de chance d'augmenter l'attaque du lanceur d'un cran ",60.0,0,95,35,0)
   def use(self):
      pass