from move import AbstractMove

class ecras_face (AbstractMove):
   def __init__(self):
       super.__init__("Ecras'face","NORMAL","PHYSICAL","Ecrase l'ennemie avec les pattes ou la queue.",40.0,1,00,35,0)
   def use(self):
      pass