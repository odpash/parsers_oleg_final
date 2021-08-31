import sys

import os

INTERP = os.path.expanduser("/var/www/u1449507/data/pyth3/bin/python")
if sys.executable != INTERP:
   os.execl(INTERP, INTERP, *sys.argv)

sys.path.append(os.getcwd())

from flask_app import application