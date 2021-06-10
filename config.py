import os
import inspect
# screen
SCREEN_HEIGHT = 400
SCREEN_WIDTH = 800

# assets
scriptPATH = os.path.abspath(inspect.getsourcefile(
    lambda: 0))  # compatible interactive Python Shell
scriptDIR = os.path.dirname(scriptPATH)
assets = os.path.join(scriptDIR, "data")
