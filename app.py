from flask import Flask, render_template

app = Flask(__name__)

# index page
@app.route("/")
def index():
  return render_template('index.html')

# login page
@app.route("/login")
def login():
  return render_template('login.html')

# signup page
@app.route("/signup")
def signup():
  return render_template('signup.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)