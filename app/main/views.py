from flask import app, render_template


@app.route('/')
def index():
    print('hello there')