#!/usr/bin/python3
"""
<<<<<<< HEAD
Begins a Flask web application
=======
start Flask application
>>>>>>> 57d8f958df2861ab9918d98864cfbc158069c4cb
"""

from flask import Flask
app = Flask(__name__)

<<<<<<< HEAD
=======

>>>>>>> 57d8f958df2861ab9918d98864cfbc158069c4cb
@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'

<<<<<<< HEAD
=======

>>>>>>> 57d8f958df2861ab9918d98864cfbc158069c4cb
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return 'HBNB'

<<<<<<< HEAD
@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """Shows “C ” followed by the value of the text variable"""
    return 'C ' + text.replace('_', ' ')

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """Shows “Python ”, followed by the value of the text variable"""
    return 'Python ' + text.replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
=======

@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """display “C ” followed by the value of the text variable"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """display “Python ”, followed by the value of the text variable"""
    return 'Python ' + text.replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
>>>>>>> 57d8f958df2861ab9918d98864cfbc158069c4cb
