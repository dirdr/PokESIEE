from move import AbstractMove

class damocles (AbstractMove):
   def __init__(self):
       super.__init__("Damocles","NORMAL","PHYSICAL","Le lanceur jette violement son corps sur l'ennemie et s'inflige des degats.",120.0,1,00,10, -1/3)
   def use(self):
      pass