from move import AbstractMove

class eclair (AbstractMove):
   def __init__(self):
       super.__init__("Eclair","ELECTRIC","SPECIAL","Produit un eclair qui s'abat sur l'ennemie.",40.0,1,00,30,0)
   def use(self):
      pass