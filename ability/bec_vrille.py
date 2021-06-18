from move import AbstractMove

class bec_vrille (AbstractMove):
   def __init__(self):
       super.__init__("Bec vrille","FLYING","PHYSICAL","Une attaque utilisant le bec comme une perceuse.",80.0,1,00,20,0)
   def use(self):
      pass