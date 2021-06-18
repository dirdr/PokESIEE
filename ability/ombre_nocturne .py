from move import AbstractMove

class ombre_nocturne  (AbstractMove):
   def __init__(self):
       super.__init__("Ombre nocturne ","GHOST","SPECIAL ","Le lanceur invoque un mirage. ",60.0,1,00,15,0)
   def use(self):
      pass