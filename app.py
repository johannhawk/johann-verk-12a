from bottle import *
from sys import argv
@route("/")
def index():
  return """<h1>Johann er komminn a Heroku</h1>"""

run(host='0.0.0.0', port=argv[1])
