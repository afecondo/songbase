from flask import Flask    #need these two lines
app = Flask(__name__)

@app.route('/')     #to create route in Flask, use the @ sign
def home():         #function
    return '<h1>hello world!!!!</h1>'

@app.route('/user/<string:name>/')     #defining a route with variable
def get_user(name):
    return '<h1>hello %s your age is %d</h1>' % (name, 3)


if __name__ == '__main__':      #creates an entry point for your program to run
    app.run(debug=True)        #app.run(host='0.0.0.0', port=1216) to host publically, must use port larger than 1024
