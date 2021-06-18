from move import AbstractMove

class psyko (AbstractMove):
   def __init__(self):
       super.__init__("Psyko","PSYCHIC","SPECIAL","Une puissante force télékinétique frappe l'ennemi. 10% de chance de baisser la def spe de l'ennemie.",90.0,1,00,10,0)
   def use(self):
      pass