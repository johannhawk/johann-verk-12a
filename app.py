from bottle import *
print("Johann er komin a heroku")
run(app = app,host='0.0.0.0', port=argv[1], debug=True)
