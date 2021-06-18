from move import AbstractMove

class explonuit (AbstractMove):
   def __init__(self):
       super.__init__("Explonuit","DARK","SPECIAL","Le lanceur attaque l'ennemi avec une onde de choc ténébreuse. 10% de chance de baisser l'attaque ennemie.",85.0,0,90,10,0)
   def use(self):
      pass