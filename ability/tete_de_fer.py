from move import AbstractMove

class tete_de_fer (AbstractMove):
   def __init__(self):
       super.__init__("Tete de fer","STEEL","PHYSICAL","Le lanceur durcit sa tete pour ensuite mettre un coup de boule avec.",80.0,1,00,15,0)
   def use(self):
      pass