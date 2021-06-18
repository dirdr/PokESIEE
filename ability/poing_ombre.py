from move import AbstractMove

class poing_ombre (AbstractMove):
   def __init__(self):
       super.__init__("Poing ombre","GHOST","PHYSICAL","Le lanceur surgit des ombres et donne un coup de poing.",60.0,1,00,20,0)
   def use(self):
      pass