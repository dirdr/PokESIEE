from move import AbstractMove

class chatiment  (AbstractMove):
   def __init__(self):
       super.__init__("Chatiment ","GHOST","SPECIAL","Attaque acharn�e qui cause davantage de d�g�ts � l'ennemi s'il a un probl�me de statut. (degat double)",65.0,1,00,10,0)
   def use(self):
      pass