from move import AbstractMove

class puredepois (AbstractMove):
   def __init__(self):
       super.__init__("Pur�depois","POISON","SPECIAL","Le lanceur attaque � l'aide d'une �ruption de gaz r�pugnants. 50% de chance d'empoisonner.",30.0,0,70,20,0)
   def use(self):
      pass