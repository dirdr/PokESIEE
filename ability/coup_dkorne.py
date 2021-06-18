from move import AbstractMove

class coup_dkorne (AbstractMove):
   def __init__(self):
       super.__init__("Coup d'corne ","NORMAL","PHYSICAL","le lanceur donne un coup avec sa corne  a  l'ennemie.",65.0,1,00,25,0)
   def use(self):
      pass