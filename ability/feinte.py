from move import AbstractMove

class feinte (AbstractMove):
   def __init__(self):
       super.__init__("Feinte","DARK","PHYSICAL ","Le lanceur ruse pour feinte l'ennemie et l'attaque ensuite.",60.0,1,00,20,0)
   def use(self):
      pass