from flask import render_template
from . import app

@app.route('/')
def about():
    return render_template('about.html')

@app.route('/dogs')
def dogs():
    return render_template('dogs.html')

@app.route('/cats')
def cats():
    return render_template('cats.html')

@app.route('/fish')
def fish():
    return render_template('fish.html')

@app.route('/reptiles')
def reptiles():
    return render_template('reptiles.html')