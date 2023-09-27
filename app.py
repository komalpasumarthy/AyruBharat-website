from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from database import get_data, get_disease

# Replace with your actual values
# DATABASE_USER = 'sql9649376'
# DATABASE_PASSWORD = 'YPvLIfRIHG'
# DATABASE_NAME = 'sql9649376'
# INSTANCE_CONNECTION_NAME = 'sql9649376'

# app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@/{DATABASE_NAME}?unix_socket=/cloudsql/{INSTANCE_CONNECTION_NAME}'
# db = SQLAlchemy(app)

app = Flask(__name__)

# class Symptoms(db.Model):
#     Symptom = db.Column(db.VARCHAR(255))
#     AyurTerm = db.Column(db.VARCHAR(255))

#     def __repr__(self):
#         return '<Symptoms %r>' % self.AyurTerm


# index page
@app.route("/", methods=['GET','POST'])
def index():
  if request.method == 'POST':
    disease = request.form.get('disease')
    symptoms = request.form.get('symptoms')

  # Search the related data from the database
    results = get_disease(disease, symptoms)
        
    return render_template('results.html', users=results)
  

    
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