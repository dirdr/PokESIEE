from move import AbstractMove

class rapace  (AbstractMove):
   def __init__(self):
       super.__init__("Rapace ","FLYING","PHYSICAL","Le lanceur replie ses ailes et charge en rase-mottes. Inflige 1/3 des degats au lanceurs ",120.0,1,00,15, -1/3)
   def use(self):
      pass