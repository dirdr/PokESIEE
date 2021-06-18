from move import AbstractMove

class croc_elec (AbstractMove):
   def __init__(self):
       super.__init__("Croc élec","ELECTRIC","PHYSICAL","Le lanceur utilise une morsure électrifiée. 10% de chance d'infliger la paralysie.",65.0,0,95,15,0)
   def use(self):
      pass