from move import AbstractMove

class mega_sangsue (AbstractMove):
   def __init__(self):
       super.__init__("Méga_sangsue","GRASS","SPECIAL","Draine l'energie de l'ennemie et redonne de la vie au lanceur.",40.0,1,00,15, +1/2)
   def use(self):
      pass