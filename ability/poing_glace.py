from move import AbstractMove

class poing_glace (AbstractMove):
   def __init__(self):
       super.__init__("Poing glace ","ICE","PHYSICAL","Un coup de poing glacé vient frapper l'ennemi. 10% de chance de geler.",75.0,1,00,15,0)
   def use(self):
      pass