from move import AbstractMove

class vent_violent (AbstractMove):
   def __init__(self):
       super.__init__("Vent violent","FLYING","SPECIAL","Le lanceur déclenche une tempête de vents violents qui s'abat sur l'ennemi.",110.0,0,75,10,0)
   def use(self):
      pass