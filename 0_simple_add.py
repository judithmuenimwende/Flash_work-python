from flask import Flask
from flask import request
app = Flask(__name__)
@app.route('/square')
def index(num = 0):
  num = int(request.args.get('num',num))
  num_squared = num * num
  return "Square of {} is {}".format(num,num_squared)

if __name__ == '__main__':
  app.run(host='0.0.0.0',port=8080)