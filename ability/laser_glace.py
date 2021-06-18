from move import AbstractMove

class laser_glace (AbstractMove):
   def __init__(self):
       super.__init__("Laser glace ","ICE","SPECIAL","Lance un laser gelé sur l'ennemie. 10% de chance de geler.",90.0,1,00,15,0)
   def use(self):
      pass