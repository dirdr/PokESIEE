from move import AbstractMove

class piqure (AbstractMove):
   def __init__(self):
       super.__init__("Piqure","BUG","PHYSICAL","Le lanceur pique l'ennemie.",60.0,1,00,20,0)
   def use(self):
      pass