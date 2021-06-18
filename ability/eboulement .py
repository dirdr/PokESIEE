from move import AbstractMove

class eboulement  (AbstractMove):
   def __init__(self):
       super.__init__("Eboulement ","ROCK","PHYSICAL","Envoie de gros rochers sur l'ennemi pour infliger des dégâts.",75.0,0,90,10,0)
   def use(self):
      pass