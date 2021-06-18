from move import AbstractMove

class feuillemagik (AbstractMove):
   def __init__(self):
       super.__init__("Feuillemagik","GRASS","SPECIAL","Le lanceur disperse d'étranges feuilles qui poursuivent l'ennemi.",60.0,1,00,20,0)
   def use(self):
      pass