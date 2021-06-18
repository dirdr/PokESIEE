from move import AbstractMove

class poing_feu (AbstractMove):
   def __init__(self):
       super.__init__("Poing feu ","FIRE","PHYSICAL","Un coup de poing enflammé vient frapper l'ennemi. 10% de chance d'infliger la brulure.",75.0,1,00,15,0)
   def use(self):
      pass