from flask import Flask,redirect,url_for,render_template
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/click' , methods = ['POST','GET'])
def click():
    return render_template('searchplayers.html')

if __name__ == '__main__':
    app.run(debug=True)
