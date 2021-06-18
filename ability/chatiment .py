from move import AbstractMove

class chatiment  (AbstractMove):
   def __init__(self):
       super.__init__("Chatiment ","GHOST","SPECIAL","Attaque acharnée qui cause davantage de dégâts à l'ennemi s'il a un problème de statut. (degat double)",65.0,1,00,10,0)
   def use(self):
      pass