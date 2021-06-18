from move import AbstractMove

class buldoboule (AbstractMove):
   def __init__(self):
       super.__init__("Buldoboule","BUG","PHYSICAL","Le lanceur se roule en boule et écrase son ennemi.",65.0,1,00,15,0)
   def use(self):
      pass