from move import AbstractMove

class tonnerre (AbstractMove):
   def __init__(self):
       super.__init__("Tonnerre","ELECTRIC","SPECIAL","Une grosse decharge electrique s'abat sur l'ennemie. 10% de chance d'infliger la paralysie. ",90.0,1,00,15,0)
   def use(self):
      pass