from move import AbstractMove

class vol_vie (AbstractMove):
   def __init__(self):
       super.__init__("Vol-vie","GRASS","SPECIAL","Draine la vie de l'ennemie ce qui en redonne au lanceur.",20.0,1,00,25, +1/2)
   def use(self):
      pass