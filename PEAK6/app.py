#This is commented by ravi moluguri
#with the help if Mr.Sadam
from flask import Flask 

app = Flask(__name__)

@app.route("/")
def index():
  return "Hello World!"

if __name__ == "__main__":
  app.run(host='0.0.0.0',port=5000)
