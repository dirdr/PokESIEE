from move import AbstractMove

class close_combat  (AbstractMove):
   def __init__(self):
       super.__init__("Close combat ","FIGHTING","PHYSICAL","Le lanceur combat au corps � corps sans se prot�ger. Baisse aussi sa D�fense et sa D�fense Sp�ciale.",120.0,1,00,5,0)
   def use(self):
      pass