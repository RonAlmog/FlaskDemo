from flask import Flask, render_template, url_for, flash, redirect
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

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))      
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
      if form.email.data == 'admin@blog.com' and form.password.data == '123':
        flash('You have logged in!', 'success')
        return redirect(url_for('home'))
      else:
        flash('Login unsuccessful. Please check your user name and password.', 'danger')
    return render_template('login.html', title='Login', form=form)  

@app.route("/about")
def about():  
    return render_template('about.html', title='Abouttt')



if __name__ == '__main__':
    app.run(debug=True)