import pandas as pd
import os
import inspect


scriptPATH = os.path.abspath(inspect.getsourcefile(lambda: 0))  # compatible interactive Python Shell
scriptDIR = os.path.dirname(scriptPATH)
# for f in os.listdir("/"):
#   print(f)

f = pd.read_csv(os.path.join(scriptDIR,'poke_abilitys.csv'),';')
#print(f.loc[0])

for i in range(0,121):
    t = f.loc[i]
    test = open(os.path.join(scriptDIR,f'{t[0]}.py'),'x')

    test.write('from move import AbstractMove'+"\n"+"\n")
    test.write(f'class {t[0]} (AbstractMove):'+"\n")
    test.write(f'   def __init__(self):'+"\n")
    test.write(f'       super.__init__("{t[1]}","{t[2]}","{t[3]}","{t[4]}",{t[5]},{t[6]},{t[7]},{t[8]})'+"\n")
    test.write('   def use(self):'+"\n"+'      pass')
    test.close()