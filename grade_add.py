from flask import Flask
from flask import request
app = Flask(__name__)
@app.route('/grader')
def mark(marks="0"):
  marks=int(request.args.get('marks',marks))
  total_marks = int(marks)
  if marks>71:
    return 'A'
  elif marks>61:
    return 'B'
  elif marks>51:
    return 'C'
  else:
    return 'D'
  
  return "for marks {} the grade  is {}".format(marks,total_marks)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)