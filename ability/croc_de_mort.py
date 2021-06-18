from move import AbstractMove

class croc_de_mort (AbstractMove):
   def __init__(self):
       super.__init__("Croc de mort","NORMAL","PHYSICAL","Le lanceur mord l'ennemi à l'aide de ses incisives aiguisées.",80.0,0,90,15,0)
   def use(self):
      pass