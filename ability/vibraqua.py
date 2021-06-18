from move import AbstractMove

class vibraqua (AbstractMove):
   def __init__(self):
       super.__init__("Vibraqua","WATER","SPECIAL","Le lanceur envoie un puissant jet d'eau sur l'ennemi.",60.0,1,00,20,0)
   def use(self):
      pass