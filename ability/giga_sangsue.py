from move import AbstractMove

class giga_sangsue (AbstractMove):
   def __init__(self):
       super.__init__("Giga_sangsue","GRASS","SPECIAL","Draine l'énergie vitale de l'ennemie et en redonne au lanceur.",60.0,1,00,15, +1/2)
   def use(self):
      pass