from move import AbstractMove

class hydrocanon (AbstractMove):
   def __init__(self):
       super.__init__("Hydrocanon","WATER","SPECIAL","Un puissant jet d'eau est projeté sur l'ennemie.",110.0,0,80,5,0)
   def use(self):
      pass