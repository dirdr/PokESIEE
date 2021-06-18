from move import AbstractMove

class coup_bas (AbstractMove):
   def __init__(self):
       super.__init__("Coup bas ","DARK","PHYSICAL","Le lanceur prepare un mauvais coup rapide a l'ennemie.",70.0,1,00,5,0)
   def use(self):
      pass