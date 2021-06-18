from move import AbstractMove

class ouragan (AbstractMove):
   def __init__(self):
       super.__init__("Ouragan","FLYING","SPECIAL","Déclenche un terrible ouragan sur l'ennemie.",40.0,1,00,35,0)
   def use(self):
      pass