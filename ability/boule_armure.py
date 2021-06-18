from move import AbstractMove

class boule_armure (AbstractMove):
   def __init__(self):
       super.__init__("Boule'armure","NORMAL","STATUS","Le lanceur se met en boule et augmente sa defense d'un cran.",0.0,1,00,30,0)
   def use(self):
      pass