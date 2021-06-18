from move import AbstractMove

class bulle_do (AbstractMove):
   def __init__(self):
       super.__init__("Bulle d'o","WATER","SPECIAL","Des bulles sont envoyées avec puissance sur l'ennemi. 20% de chance de baisser la vitesse ennemie.",65.0,1,00,20,0)
   def use(self):
      pass