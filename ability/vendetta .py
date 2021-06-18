from move import AbstractMove

class vendetta  (AbstractMove):
   def __init__(self):
       super.__init__("Vendetta","FIGHTING","PHYSICAL","Le lanceur se venge de l'adversaire avec un puissant coup montant. Degat double si le lanceur attaque en second.",60.0,1,00,20,0)
   def use(self):
      pass