from move import AbstractMove

class belier (AbstractMove):
   def __init__(self):
       super.__init__("B�lier","NORMAL","PHYSICAL","Une charge violente qui blesse aussi le lanceur  d' 1/4 des degats qu'il a inflig�.",90.0,0,85,20, -1/4)
   def use(self):
      pass