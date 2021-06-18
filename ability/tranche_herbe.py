from move import AbstractMove

class tranche_herbe (AbstractMove):
   def __init__(self):
       super.__init__("Tranch'herbe","GRASS","PHYSICAL","Des feuilles aiguisées comme des rasoirs entaillent l'ennemi.",55.0,0,95,25,0)
   def use(self):
      pass