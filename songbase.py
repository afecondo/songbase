from flask import Flask, render_template    #need these two lines
app = Flask(__name__)


@app.route('/')     #to create route in Flask, use the @ sign
def index():         #function
    #return '<h1>hello world!!!! lalala </h1>'
    return render_template('index.html')

@app.route('/songs')
def get_all_songs():
    songs = [
        'Baba O Reilly',
        'Eh Cumpari',
        'Fly me to the Moon'
    ]
    return render_template('songs.html', songs=songs)

@app.route('/user/<string:name>/')     #defining a route with variable
def get_user_name(name):
    #return '<h1>hello %s your age is %d</h1>' % (name, 3)
    return render_template('user.html', user_name=name)

if __name__ == '__main__':      #creates an entry point for your program to run
    app.run()        #app.run(host='0.0.0.0', port=1216) to host publically, must use port larger than 1024
