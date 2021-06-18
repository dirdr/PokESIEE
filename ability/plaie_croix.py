from move import AbstractMove

class plaie_croix (AbstractMove):
   def __init__(self):
       super.__init__("Plaie-croix","BUG","PHYSICAL","Le lanceur taillade l'ennemi en utilisant ses faux ou ses griffes comme une paire de ciseaux.",80.0,1,00,15,0)
   def use(self):
      pass