from move import AbstractMove

class pietisol (AbstractMove):
   def __init__(self):
       super.__init__("Piétisol","GROUND","PHYSICAL ","Le lanceur piétine le sol et inflige des dégâts à tous les Pokémon autour de lui.",60.0,1,00,20,0)
   def use(self):
      pass