from move import AbstractMove

class direct_toxic (AbstractMove):
   def __init__(self):
       super.__init__("Direct toxic ","POISON","PHYSICAL","Attaque l'ennemi avec un tentacule, un bras, ou un autre membre plein de poison. 30% de chance d'empoisonner.",80.0,1,00,20,0)
   def use(self):
      pass