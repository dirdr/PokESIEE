from move import AbstractMove

class close_combat  (AbstractMove):
   def __init__(self):
       super.__init__("Close combat ","FIGHTING","PHYSICAL","Le lanceur combat au corps à corps sans se protéger. Baisse aussi sa Défense et sa Défense Spéciale.",120.0,1,00,5,0)
   def use(self):
      pass