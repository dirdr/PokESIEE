from move import AbstractMove

class tempete_florale (AbstractMove):
   def __init__(self):
       super.__init__("Tempete florale","GRASS","PHYSICAL","Déclenche une violente tempête de fleurs qui inflige des dégâts.",90.0,1,00,15,0)
   def use(self):
      pass