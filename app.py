from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from database import get_data, get_disease

app = Flask(__name__)

# index page
@app.route("/", methods=['GET','POST'])
def index():
  if request.method == 'POST':
    disease = request.form.get('disease')
    symptoms = request.form.get('symptoms')

  # Search the related data from the database
    results = get_disease(disease, symptoms)
        
    return render_template('result.html', users=results)
  

    
  return render_template('index.html')

# login page
@app.route("/login")
def login():
  return render_template('login.html')

# signup page
@app.route("/signup")
def signup():
  return render_template('signup.html')

@app.route('/result')
def results():
  data = get_data()
  return render_template('result.html', users=data)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)