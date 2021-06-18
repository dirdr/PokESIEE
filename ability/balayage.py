from move import AbstractMove

class balayage (AbstractMove):
   def __init__(self):
       super.__init__("Balayage","FIGHTING","PHYSICAL","Un puissant coup de pied bas qui fauche l'ennemi. Inflige des degats en fct du niveau du pokemon.",nan,1,00,25,0)
   def use(self):
      pass