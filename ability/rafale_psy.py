from move import AbstractMove

class rafale_psy (AbstractMove):
   def __init__(self):
       super.__init__("Rafale psy","PSYCHIC","SPECIAL","Un étrange rayon frappe l'ennemi.",65.0,1,00,20,0)
   def use(self):
      pass