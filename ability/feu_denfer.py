from move import AbstractMove

class feu_denfer (AbstractMove):
   def __init__(self):
       super.__init__("Feu d'enfer","FIRE","SPECIAL","L'ennemi est entouré d'un torrent de flammes ardentes qui le brûlent obligatoirement.",100.0,0,50,5,0)
   def use(self):
      pass