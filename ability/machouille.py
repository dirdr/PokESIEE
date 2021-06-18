from move import AbstractMove

class machouille (AbstractMove):
   def __init__(self):
       super.__init__("Machouille","DARK","PHYSICAL","Le lanceur machouille l'ennemie avec ses crocs.",80.0,1,00,15,0)
   def use(self):
      pass