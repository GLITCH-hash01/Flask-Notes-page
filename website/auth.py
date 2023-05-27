from flask import Blueprint,render_template,request,flash,redirect,url_for
from werkzeug.security import generate_password_hash,check_password_hash
from .model import User
from . import db
from flask_login import login_user,login_required,current_user,logout_user


auth = Blueprint('auth',__name__)

#Login routes
@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        #To get the user details from the database to know if it exists
        user=User.query.filter_by(email=email).first()
        if user:
            # checking password if they match
            if check_password_hash(user.password,password):
                flash('Logged in successfully',category='successmessage')
                login_user(user,remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password',category='errormessage')
        else:
            flash('Email doesn"t exist',category='errormessage')

    return render_template('login.html',user=current_user)

#Logout page for user
@auth.route('/logout',methods=['GET','POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

#Signup page for user
@auth.route('/sign-up',methods=['GET','POST'])
def Signup():
    
    if request.method == 'POST':
        email=request.form.get('email')
        firstName=request.form.get('firstName')
        password1=request.form.get('password1')
        password2=request.form.get('password2')
        # To check if user already exists
        user=User.query.filter_by(email=email).first()
        #Check the standard password and other conditions
        if len(email)<8:
            flash('Email must be at least 8 characters',category='errormessage')#Used to show error message with flask
        elif len(firstName)<2:
            flash('First name must be at least 2 characters',category='errormessage')
        elif password1!=password2:
            flash('Passwords do not match',category='errormessage')
        elif len(password1)<7:
            flash('Password must be at least 8 characters',category='errormessage')
        elif user:
            flash('User already exists',category='errormessage')
        else:
            # Adds the details to the database
            new_user=User(email=email,first_name=firstName,password=generate_password_hash(password1,method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully',category='successmessage')
            login_user(new_user,remember=True)
            return redirect(url_for('views.home'))



    return render_template('sign_up.html',user=current_user)

