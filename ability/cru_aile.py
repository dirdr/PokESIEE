from move import AbstractMove

class cru_aile (AbstractMove):
   def __init__(self):
       super.__init__("Cru-aile","FLYING","PHYSICAL","L'ennemi est frappé par de larges ailes déployées pour infliger des dégâts.",65.0,1,00,35,0)
   def use(self):
      pass