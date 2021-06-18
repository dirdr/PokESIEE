from move import AbstractMove

class boutefeu (AbstractMove):
   def __init__(self):
       super.__init__("Boutefeu","FIRE","PHYSICAL","Le lanceur s'embrase et fonce violement sur sa cible. Inflige aussi des degats au lanceur.",120.0,1,00,15, -1/3)
   def use(self):
      pass