from move import AbstractMove

class represaille (AbstractMove):
   def __init__(self):
       super.__init__("Represaille","DARK","PHYSICAL","Le lanceur charge son �nergie, puis attaque. La puissance est doubl�e si le lanceur a une vitesse plus petite que l'ennemie.",50.0,1,00,10,0)
   def use(self):
      pass