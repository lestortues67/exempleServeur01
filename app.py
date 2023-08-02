
"""
Source : 
Date : 13/10/2022
Auteur : Christian Doriath
Dossier : /informatique/developpements/javascript/JS Regex regular expression
Fichier : app.py
Description : app de démonstration des regex stockées dans une table MySQL

Mot cles : 
"""

import datetime
import string
from flask import Flask, request, render_template, session, redirect, url_for, flash, jsonify
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from random import choice
import locale
import time
import os
from logging import FileHandler, WARNING

locale.setlocale(locale.LC_TIME, "fr_FR")

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'hard to guess string'


bootstrap = Bootstrap(app)

if not app.debug:
	file_handler = FileHandler('errorlog.txt')
	file_handler.setLevel(WARNING)
	app.logger.addHandler(file_handler)



@app.route('/')
def myindex():
    return render_template('index.html',title="Flask_Regex")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
