
from flask import Flask


from flask.ext.sqlalchemy import SQLAlchemy

import os, socket


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = os.environ['DATABASE_URI']
db = SQLALchemy(app)
hostname = socket.gethostname()

@app.route('/')

def index():
  return 'Hello, from visualpath IT acamedy %s!\n' % hostname

@app.route('/db')
def dbtest():

 try:

    db.create_all()

 except Exception as e:

     return e.message +'/n'
 return 'database connected from %s!\n' % hostname


if__name___  ==  '__main__':

  app.run()

