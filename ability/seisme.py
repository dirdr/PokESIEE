from move import AbstractMove

class seisme (AbstractMove):
   def __init__(self):
       super.__init__("Séisme","GROUND","PHYSICAL","Le lanceur provoque un tremblement de terre qui inflige de gros degats a l'ennemie.",100.0,1,00,10,0)
   def use(self):
      pass