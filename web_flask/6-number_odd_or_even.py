#!/usr/bin/python3
"""
<<<<<<< HEAD
starts a Flask web application
=======
start Flask application
>>>>>>> 57d8f958df2861ab9918d98864cfbc158069c4cb
"""

from flask import Flask, render_template
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
=======

>>>>>>> 57d8f958df2861ab9918d98864cfbc158069c4cb
@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """display “C ” followed by the value of the text variable"""
    return 'C ' + text.replace('_', ' ')

<<<<<<< HEAD
=======

>>>>>>> 57d8f958df2861ab9918d98864cfbc158069c4cb
@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """display “Python ”, followed by the value of the text variable"""
    return 'Python ' + text.replace('_', ' ')

<<<<<<< HEAD
=======

>>>>>>> 57d8f958df2861ab9918d98864cfbc158069c4cb
@app.route('/number/<int:n>', strict_slashes=False)
def imanumber(n):
    """display “n is a number” only if n is an integer"""
    return "{:d} is a number".format(n)

<<<<<<< HEAD
=======

>>>>>>> 57d8f958df2861ab9918d98864cfbc158069c4cb
@app.route('/number_template/<int:n>', strict_slashes=False)
def numbersandtemplates(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)

<<<<<<< HEAD
@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def numbersandevenness(n):
    """display a HTML page only if n is an integer"""
    evenness = 'even' if n % 2 == 0 else 'odd'
    return render_template('6-number_odd_or_even.html', n=n, evenness=evenness)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
=======

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def numbersandevenness(n):
    """display a HTML page only if n is an integer"""
    if n % 2 == 0:
        evenness = 'even'
    else:
        evenness = 'odd'
    return render_template('6-number_odd_or_even.html', n=n,
                           evenness=evenness)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
>>>>>>> 57d8f958df2861ab9918d98864cfbc158069c4cb
