from move import AbstractMove

class blizzard (AbstractMove):
   def __init__(self):
       super.__init__("Blizzard","ICE","SPECIAL","Deferle une tempe de glace sur le terrain. 20% de chance de geler.",110.0,0,70,5,0)
   def use(self):
      pass