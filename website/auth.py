from flask import Blueprint,render_template,request,flash

auth = Blueprint('auth',__name__)


@auth.route('/login',methods=['GET','POST'])
def login():
    return render_template('login.html')

@auth.route('/logout',methods=['GET','POST'])
def Signin():
    return '<h1>Logout</h1>'

@auth.route('/sign-up',methods=['GET','POST'])
def Signup():
    if request.method == 'POST':
        email=request.form.get('email')
        firstName=request.form.get('firstName')
        password1=request.form.get('password1')
        password2=request.form.get('password2')
        if len(email)<8:
            flash('Email must be at least 8 characters',category='errormessage')#Used to show error message with flask
        elif len(firstName)<2:
            flash('First name must be at least 2 characters',category='errormessage')
        elif password1!=password2:
            flash('Passwords do not match',category='errormessage')
        elif len(password1)<7:
            flash('Password must be at least 8 characters',category='errormessage')
        else:
            flash('Account created successfully',category='successmessage')


    return render_template('sign_up.html')