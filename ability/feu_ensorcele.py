from move import AbstractMove

class feu_ensorcele (AbstractMove):
   def __init__(self):
       super.__init__("Feu ensorcel�","FIRE","SPECIAL","Attaque avec des flammes br�lantes souffl�es de la bouche du lanceur. Diminue l'Attaque Sp�ciale de l'ennemi d'un cran.",75.0,1,00,10,0)
   def use(self):
      pass