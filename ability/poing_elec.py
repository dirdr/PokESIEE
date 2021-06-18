from move import AbstractMove

class poing_elec (AbstractMove):
   def __init__(self):
       super.__init__("Poing elec","ELECTRIC","PHYSICAL","Un coup de poing electrifié vient frapper l'ennemi. 10% de chance d'infliger la paralysie.",75.0,1,00,15,0)
   def use(self):
      pass