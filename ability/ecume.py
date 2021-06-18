from move import AbstractMove

class ecume (AbstractMove):
   def __init__(self):
       super.__init__("Ecume","WATER","SPECIAL","Une attaque de bulle. 10% de chance de baisser la vitesse ennemie.",40.0,1,00,30,0)
   def use(self):
      pass