from move import AbstractMove

class puredepois (AbstractMove):
   def __init__(self):
       super.__init__("Purédepois","POISON","SPECIAL","Le lanceur attaque à l'aide d'une éruption de gaz répugnants. 50% de chance d'empoisonner.",30.0,0,70,20,0)
   def use(self):
      pass