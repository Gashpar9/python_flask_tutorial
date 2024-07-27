from flask import render_template
from app import app
from app.forms import LoginForm

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

@app.route('/login')
def login():
    form = LoginForm()
    
    return render_template('login.html', title = 'Sign in', form = form)