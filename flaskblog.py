from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '123123'
posts = [
  {
    'author': 'Johny Smith',
    'title': 'Alice in wonderland',
    'content': 'bla bla bla',
    'date': 'april 1, 2019'
  },
  {
    'author': 'Johny Guitar',
    'title': 'Madjhull and sons',
    'content': 'kwa kwa kwaaa',
    'date': 'april 2, 2017'
  }

]

@app.route("/home")
@app.route("/")
def home():
    return render_template('home.html', posts=posts)

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)  

@app.route("/about")
def about():  
    return render_template('about.html', title='Abouttt')



if __name__ == '__main__':
    app.run(debug=True)