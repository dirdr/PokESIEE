from move import AbstractMove

class detricanon (AbstractMove):
   def __init__(self):
       super.__init__("Détricanon","POISON","PHYSICAL","Le lanceur envoie des détritus sur l'ennemi. 30% de chance d'empoisonner.",120.0,0,80,5,0)
   def use(self):
      pass