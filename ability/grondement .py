from move import AbstractMove

class grondement  (AbstractMove):
   def __init__(self):
       super.__init__("Grondement ","DARK","STATUS","Le lanceur montre sa puissance d'un grondement. Augmente son attaque d'un cran.",0.0,0,95,15,0)
   def use(self):
      pass