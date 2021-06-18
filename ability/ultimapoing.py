from move import AbstractMove

class ultimapoing (AbstractMove):
   def __init__(self):
       super.__init__("Ultimapoing","NORMAL","PHYSICAL","L'ennemi reçoit un coup de poing d'une puissance incroyable.",80.0,0,85,15,0)
   def use(self):
      pass