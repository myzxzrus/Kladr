# MVC - Model View Controller
from app import app
from flask import render_template
import os
from flask import send_from_directory

@app.route('/')
def index():
    name = 'Ivan'
    return render_template('index.html', name=name)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

#  Модуль визуализации.
