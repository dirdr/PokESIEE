from move import AbstractMove

class feu_ensorcele (AbstractMove):
   def __init__(self):
       super.__init__("Feu ensorcelé","FIRE","SPECIAL","Attaque avec des flammes brûlantes soufflées de la bouche du lanceur. Diminue l'Attaque Spéciale de l'ennemi d'un cran.",75.0,1,00,10,0)
   def use(self):
      pass