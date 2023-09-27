from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Replace with your actual values
DATABASE_USER = 'sql9649376'
DATABASE_PASSWORD = 'YPvLIfRIHG'
DATABASE_NAME = 'sql9649376'
INSTANCE_CONNECTION_NAME = 'sql9649376'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@/{DATABASE_NAME}?unix_socket=/cloudsql/{INSTANCE_CONNECTION_NAME}'
db = SQLAlchemy(app)



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