from move import AbstractMove

class vive_attaque (AbstractMove):
   def __init__(self):
       super.__init__("vive-attaque","NORMAL","PHYSICAL","Le lanceur attaque rapidement l'ennemie.",50.0,1,00,30,0)
   def use(self):
      pass