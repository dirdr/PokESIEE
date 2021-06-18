from move import AbstractMove

class queue_de_fer (AbstractMove):
   def __init__(self):
       super.__init__("Queue de fer","STEEL","PHYSICAL","Le lanceur durcit sa queue pour balayer l'ennemie avec. 30% de chance de baisser la defense ennemie.",100.0,0,75,15,0)
   def use(self):
      pass