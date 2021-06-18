from move import AbstractMove

class lame_dair (AbstractMove):
   def __init__(self):
       super.__init__("Lame d'air","FLYING","SPECIAL","Le lanceur attaque avec une lame d'air qui fend tout. ",75.0,0,90,15,0)
   def use(self):
      pass