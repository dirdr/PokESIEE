from move import AbstractMove

class pietisol (AbstractMove):
   def __init__(self):
       super.__init__("Pi�tisol","GROUND","PHYSICAL ","Le lanceur pi�tine le sol et inflige des d�g�ts � tous les Pok�mon autour de lui.",60.0,1,00,20,0)
   def use(self):
      pass