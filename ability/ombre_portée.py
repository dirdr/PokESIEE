from move import AbstractMove

class ombre_portée (AbstractMove):
   def __init__(self):
       super.__init__("Ombre portée","GHOST","SPECIAL","Le lanceur étend son ombre pour frapper par-derrière.",50.0,1,00,30,0)
   def use(self):
      pass