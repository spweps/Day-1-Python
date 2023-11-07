from flask_app import app
from flask import render_template,request,redirect,session,flash
from flask_app.models.user import User
from flask_app.models.show import Show
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/register',methods=['POST'])
def register():

    if not User.validate_register(request.form):
        return redirect('/')
    data ={ 
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.save(data)
    session['user_id'] = id

    return redirect('/dashboard')

@app.route('/login',methods=['POST'])
def login():
    user = User.get_by_email(request.form)

    if not user:
        flash("Invalid Email","login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Password","login")
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    #users=Show.get_poster()
    return render_template("dashboard.html",user=User.get_by_id(data), shows=Show.get_all()) #users=users)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route("/edit")
def edit():
    if "user_id" not in session:
        flash("Must be logged in to view page")
        return redirect("/")
        
    data = {
        "email":session["email"]
    }
    user = User.get_by_email(data)
    return render_template("edit_show.html",user=user)
