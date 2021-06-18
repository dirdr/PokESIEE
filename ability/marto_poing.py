from move import AbstractMove

class marto_poing (AbstractMove):
   def __init__(self):
       super.__init__("Marto poing ","FIGHTING","PHYSICAL","Le lanceur donne un puissant coup de poing à l'ennemi. Réduit la Vitesse du lanceur d'un cran.",100.0,0,90,10,0)
   def use(self):
      pass