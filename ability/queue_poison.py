from move import AbstractMove

class queue_poison (AbstractMove):
   def __init__(self):
       super.__init__("Queue-poison","POISON","PHYSICAL","Balaye l'ennemie avec une queue rempli de poison.",50.0,1,00,25,0)
   def use(self):
      pass