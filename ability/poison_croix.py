from move import AbstractMove

class poison_croix (AbstractMove):
   def __init__(self):
       super.__init__("Poison croix","POISON","PHYSICAL","Un coup tranchant qui peut empoisonner l'ennemi.  10% de chance d'empoisonner.",70.0,1,00,20,0)
   def use(self):
      pass