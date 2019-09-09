from flask import Flask, render_template, url_for
app = Flask(__name__)

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

@app.route("/about")
def about():  
    return render_template('about.html', title='Abouttt')



if __name__ == '__main__':
    app.run(debug=True)