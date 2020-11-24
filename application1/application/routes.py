from flask import render_template, redirect, url_for
from application import app
import requests

@app.route('/')

@app.route('/home', methods=['GET'])
def home():
    return render_template('index.html', title='Home')


@app.route('/get/animal', methods=['GET','POST'])
def animal():
    animal=requests.get('http://application2:5001/animal/name')
    noise=requests.post('http://application2:5001/animal/noise',data=animal.text)
    return render_template('animal.html',title='Animals', animal=animal.text, noise=noise.text)