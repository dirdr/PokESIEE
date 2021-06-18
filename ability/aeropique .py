from move import AbstractMove

class aeropique  (AbstractMove):
   def __init__(self):
       super.__init__("Aeropique ","FLYING","PHYSICAL","Le lanceur prend l'ennemi de vitesse et le lacère.",60.0,1,00,20,0)
   def use(self):
      pass