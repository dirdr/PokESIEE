from move import AbstractMove

class bourdon (AbstractMove):
   def __init__(self):
       super.__init__("Bourdon","BUG","SPECIAL","Le lanceur fait vibrer son corps pour lancer une vague sonique. 10% de chance de baisser la Défense Spéciale de l'ennemi.",90.0,1,00,10,0)
   def use(self):
      pass