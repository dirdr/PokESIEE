from move import AbstractMove

class etincelle (AbstractMove):
   def __init__(self):
       super.__init__("Etincelle","ELECTRIC","PHYSICAL","Lance une charge electrique sur l'ennemie. 10% de chance d'infliger la paralysie.",65.0,1,00,20,0)
   def use(self):
      pass