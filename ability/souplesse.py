from move import AbstractMove

class souplesse (AbstractMove):
   def __init__(self):
       super.__init__("Souplesse","NORMAL","PHYSICAL","Fouette l'ennemi avec la queue ou une liane, par exemple, pour infliger des dégâts.",80.0,0,75,20,0)
   def use(self):
      pass