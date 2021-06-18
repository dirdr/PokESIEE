from move import AbstractMove

class balle_ombre (AbstractMove):
   def __init__(self):
       super.__init__("Balle'ombre","GHOST","SPECIAL","Projette une grande ombre sur l'ennemi. 10% de chance de baisser la def spe de l'ennemie.",80.0,1,00,15,0)
   def use(self):
      pass