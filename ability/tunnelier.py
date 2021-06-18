from move import AbstractMove

class tunnelier (AbstractMove):
   def __init__(self):
       super.__init__("Tunnelier","GROUND","PHYSICAL","Le lanceur tourne sur lui-même comme une perceuse et se jette sur l'ennemi.",85.0,0,90,10,0)
   def use(self):
      pass