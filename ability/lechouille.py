from move import AbstractMove

class lechouille (AbstractMove):
   def __init__(self):
       super.__init__("Léchouille","GHOST","PHYSICAL","Un grand coup de langue qui inflige des dégâts à l'ennemi. 30% de chance d'infliger la paralysie ",30.0,1,00,30,0)
   def use(self):
      pass