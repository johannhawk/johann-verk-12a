from bottle import *
from sys import argv
@route("/")
def index():
  return '''Johann er komminn a Heroku'''
run(app = app,host='0.0.0.0', port=argv[1], debug=True)
