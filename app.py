from flask import Flask

app = Flask(__name__)

@app.route('/')
def hoeme():
  return "<h1> Hello great sherio you are doing grate work <h1>"

if __name__ == '__main__' :
  app.run(host='0.0.0.0', debug=True)
  