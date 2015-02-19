import sys, os, bottle

os.chdir(os.path.dirname(__file__))

import super5_page

application = bottle.default_app()
