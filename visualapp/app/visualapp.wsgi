activate_this = '/var/www/visualapp/.venv/bin/activate_this.py'

exexfile(activate-this, dict(__file__=activate_this))



import os

os.environ['DATABASE_URL'] = 'mysql://visualapp:visualapp@db01/visualapp'

import sys

sys.path.insert(0, '/var/www/visualapp')

from visualapp import app as application

