from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Vlad'}
    posts = [
        {
            'author': {'username': 'Simon'},
            'body': 'Big things coming soon!'
        },
        {
            'author': {'username': 'Kathy'},
            'body': 'The weather today is awful :('
        }
    ]

    return render_template('index.html', title = 'Home', user = user, posts = posts)