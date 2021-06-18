from move import AbstractMove

class lame_feuille (AbstractMove):
   def __init__(self):
       super.__init__("Lame-feuille","GRASS","PHYSICAL","Une feuille coupante comme une lame entaille l'ennemie.",75.0,1,00,15,0)
   def use(self):
      pass