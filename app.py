from flask import Flask, render_template, request, redirect, url_for, flash

from database import get_data, get_disease, insert_user, check_user


app = Flask(__name__)

# index page
@app.route("/", methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    disease = request.form.get('disease')
    symptoms = request.form.get('symptoms')
    results = get_disease(disease, symptoms)
    return render_template('result.html', users=results)

  return render_template('index.html')


# login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
          
        user_exists, password_correct = check_user(email, password)
        if user_exists:
            if password_correct:
                return redirect(url_for('index'))
            else:
                flash('Wrong password')
        else:
            flash('No user found')
    return render_template('login.html')


# signup page
@app.route("/signup", methods=['GET','POST'])
def signup():
  if request.method == 'POST':
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phoneno')
    # gender = request.form.get('gender')
    password = request.form.get('password')

    insert_user(name, email, phone, password)
    return redirect(url_for('login'))

  return render_template('signup.html')


@app.route('/result')
def results():
  data = get_data()
  return render_template('result.html', users=data)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
