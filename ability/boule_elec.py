from move import AbstractMove

class boule_elec (AbstractMove):
   def __init__(self):
       super.__init__("Boule elec","ELECTRIC","SPECIAL","Le lanceur envoie une boule d'électricité. Si sa vitesse est plus grande que l'ennemie, la puissance est doublé.",50.0,1,00,10,0)
   def use(self):
      pass