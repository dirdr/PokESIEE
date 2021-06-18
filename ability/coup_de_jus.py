from move import AbstractMove

class coup_de_jus (AbstractMove):
   def __init__(self):
       super.__init__("Coup de jus ","ELECTRIC","SPECIAL","Un flamboiement d'électricité frappe l'ennemie. 30% de chance d'infliger la paralysie.",80.0,1,00,15,0)
   def use(self):
      pass