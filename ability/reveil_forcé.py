from move import AbstractMove

class reveil_forcé (AbstractMove):
   def __init__(self):
       super.__init__("Reveil forcé","FIGHTING","PHYSICAL","Le lanceur gifle le pokemon ennemie comme pour le reveiller.",70.0,1,00,20,0)
   def use(self):
      pass