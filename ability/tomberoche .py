from move import AbstractMove

class tomberoche  (AbstractMove):
   def __init__(self):
       super.__init__("Tomberoche ","ROCK","PHYSICAL","Des rochers frappent l'ennemi. Réduit aussi sa Vitesse d'un cran.",60.0,0,95,15,0)
   def use(self):
      pass