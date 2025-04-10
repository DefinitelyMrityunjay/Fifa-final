from flask import Flask
app = Flask(__name__)


@app.route('/')
def welcome():
    return "hi this is mj"

@app.route('/members')
def wtf():
    return "omggee"

if __name__ == '__main__':
    app.run(debug=True)