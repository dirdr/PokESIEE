from move import AbstractMove

class peignee (AbstractMove):
   def __init__(self):
       super.__init__("Peignee","NORMAL","PHYSICAL ","Le lanceur donne un coup avec sa t�te couronn�e d'une fi�re crini�re. Inflige aussi 1/4 des degats au lanceur.",120.0,1,00,15, -1/4)
   def use(self):
      pass