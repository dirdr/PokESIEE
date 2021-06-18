from move import AbstractMove

class rayon_signal (AbstractMove):
   def __init__(self):
       super.__init__("Rayon signal ","BUG","SPECIAL","Un étrange rayon...",75.0,1,00,15,0)
   def use(self):
      pass