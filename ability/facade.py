from move import AbstractMove

class facade (AbstractMove):
   def __init__(self):
       super.__init__("Façade","NORMAL","PHYSICAL","Attaque qui inflige le double de degats le lanceur est affecte par un probleme de status.",70.0,1,00,20,0)
   def use(self):
      pass