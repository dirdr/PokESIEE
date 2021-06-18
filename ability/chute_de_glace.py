from move import AbstractMove

class chute_de_glace (AbstractMove):
   def __init__(self):
       super.__init__("Chute de glace ","ICE","PHYSIC ","Envoie de gros blocs de glace sur l'ennemi pour lui infliger des dégâts. 30% de chance de baisser la defense ennemie.",80.0,0,95,10,0)
   def use(self):
      pass