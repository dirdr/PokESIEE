from move import AbstractMove

class vent_glace  (AbstractMove):
   def __init__(self):
       super.__init__("Vent glace ","ICE","SPECIAL","Un vent du nord tellment froid qu'il fait baisser la vitesse de l'ennemie d'un cran.",55.0,0,95,25,0)
   def use(self):
      pass