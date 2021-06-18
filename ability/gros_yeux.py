from move import AbstractMove

class gros_yeux (AbstractMove):
   def __init__(self):
       super.__init__("Gros'yeux","NORMAL","STATUS","Intimide l'ennemie d'un regarde ce qui lui fais baisser sa defense d'un cran.",0.0,1,00,40,0)
   def use(self):
      pass