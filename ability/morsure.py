from move import AbstractMove

class morsure (AbstractMove):
   def __init__(self):
       super.__init__("Morsure","DARK","PHYSICAL","Le lanceur mort l'ennemie avec ses crocs.",60.0,1,00,25,0)
   def use(self):
      pass