from move import AbstractMove

class casse_brique  (AbstractMove):
   def __init__(self):
       super.__init__("Casse-brique ","FIGHTING","PHYSICAL","Le lanceur attaque avec le tranchant de la main. ",75.0,1,00,15,0)
   def use(self):
      pass