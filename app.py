from flask import Flask, render_template, request, redirect, url_for, flash

import database

app = Flask(__name__)


# index page
@app.route("/", methods=['GET', 'POST'])
def homepage():
  return render_template('homePage.html')

# input page
@app.route('/input', methods=['GET','POST'])
def inputpage():
  if request.method == 'POST':
    symptoms = request.form.get('symptoms')
    if (symptoms):
      data = database.get_disease(symptoms)
      return render_template('outputpage.html', result = data)
    return redirect(url_for('outputpage'))
  return render_template('inputpage.html')



# result page
@app.route('/result')
def outputpage():
  return render_template('outputpage.html')


# login page
@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    email = request.form.get('email')
    password = request.form.get('password')

    user_exists, password_correct = database.check_user(email, password)
    if user_exists:
      if password_correct:
        return redirect(url_for('index'))
      else:
        flash('Wrong password')
    else:
      flash('No user found')
  return render_template('login.html')


# signup page
@app.route("/signup", methods=['GET', 'POST'])
def signup():
  if request.method == 'POST':
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phoneno')
    # gender = request.form.get('gender')
    password = request.form.get('password')

    database.insert_user(name, email, phone, password)
    return redirect(url_for('login'))

  return render_template('signup.html')



if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
