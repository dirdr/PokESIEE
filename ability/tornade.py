from move import AbstractMove

class tornade (AbstractMove):
   def __init__(self):
       super.__init__("Tornade","FLYING","SPECIAL","Le lanceur bat des ailes pour générer une bourrasque qui blesse l'ennemi.",40.0,1,00,35,0)
   def use(self):
      pass