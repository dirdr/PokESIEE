from move import AbstractMove

class dard_venin (AbstractMove):
   def __init__(self):
       super.__init__("Dard-venin","POISON","PHYSICAL","Le lanceur projette une dard gorgée de venin. 30% de chance d'infliger l'empoisennement ",15.0,1,00,35,0)
   def use(self):
      pass