from flask import Flask
from flask import request
app = Flask(__name__)
@app.route('/')
def index(name = "Student"):
  name = request.args
  return "Welcome {}".format(name)

@app.route('/home')
def home():
  return "Welcome Home"

if __name__ == '__main__':
  app.run(host='0.0.0.0',port=8080)