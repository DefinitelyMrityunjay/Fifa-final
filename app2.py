from flask import Flask 


app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to my page" 

@app.route("/success/<score>")
def success(score):
    return "You have passed and you score is " + score


if __name__ == "__main__" :
    app.run(debug=True)