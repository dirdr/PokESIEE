from move import AbstractMove

class attrition (AbstractMove):
   def __init__(self):
       super.__init__("Attrition","NORMAL","PHYSICAL","Une attaque puissante quand l’ennemi baisse sa garde.",70.0,1,00,20,0)
   def use(self):
      pass