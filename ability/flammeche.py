from move import AbstractMove

class flammeche (AbstractMove):
   def __init__(self):
       super.__init__("Flamm�che","FIRE","SPECIAL","L'ennemie est attaqu�e par une faible flamme.  10% de chance d'infliger la brulure .",40.0,1,00,25,0)
   def use(self):
      pass