from move import AbstractMove

class uppercut (AbstractMove):
   def __init__(self):
       super.__init__("Uppercut","NORMAL","PHYSICAL","Un coup de poing cadencé.",70.0,1,00,15,0)
   def use(self):
      pass