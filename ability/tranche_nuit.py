from move import AbstractMove

class tranche_nuit (AbstractMove):
   def __init__(self):
       super.__init__("Tranche nuit ","DARK","PHYSICAL","Le lanceur lac�re l'ennemi � la premi�re occasion. ",70.0,1,00,15,0)
   def use(self):
      pass