from move import AbstractMove

class saumure (AbstractMove):
   def __init__(self):
       super.__init__("Saumure","WATER","SPECIAL","Attaque qui voit sa puissance doublé si les pv du lanceur sont en dessous de 50%.",65.0,1,00,10,0)
   def use(self):
      pass