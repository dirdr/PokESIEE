from move import AbstractMove

class picpic (AbstractMove):
   def __init__(self):
       super.__init__("Picpic","FLYING","PHYSICAL","Frappe l'ennemi d'un bec pointu ou d'une corne pour infliger des dégâts.",35.0,1,00,30,0)
   def use(self):
      pass