import os, flask
PORT = int(os.environ['PORT'])
app = flask.Flask('app server')
@app.route('/')
def index():
  return 'hello Dockerfile3'
app.run(debug=False, host='0.0.0.0', port=PORT)
