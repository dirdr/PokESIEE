from move import AbstractMove

class double_pied (AbstractMove):
   def __init__(self):
       super.__init__("Double pied","FIGHTING","PHYSICAL","Le lanceur attaque avec son pied deux fois.",40.0,1,00,30,0)
   def use(self):
      pass