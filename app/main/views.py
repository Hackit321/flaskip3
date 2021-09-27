from app.models import Pitch
from flask import render_template, redirect, url_for,abort,request
from . import main
from flask_login import login_required,current_user



@main.route('/')
def index():
    pitches = Pitch.query.all()
    job = Pitch.query.filter_by(category = 'Job').all() 
    event = Pitch.query.filter_by(category = 'Events').all()
    advertisement = Pitch.query.filter_by(category = 'Advertisement').all()
    return render_template('index.html', job = job,event = event, pitches = pitches,advertisement= advertisement)
