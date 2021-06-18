from move import AbstractMove

class vibrobscure (AbstractMove):
   def __init__(self):
       super.__init__("Vibrobscure","DARK","SPECIAL","Le lanceur dégage une horrible aura chargée de pensées maléfiques. ",80.0,1,00,15,0)
   def use(self):
      pass