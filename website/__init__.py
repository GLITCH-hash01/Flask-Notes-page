from flask import Flask
from flask_sqlalchemy import SQLAlchemy #For accessing the database and working on it 
from flask_login import LoginManager #For keeping track of Login and Logouts


db=SQLAlchemy()


def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY'] ='hkjadkfasdfasdfasdfasdfasdfasdfasdfasdfasdf'# secret key for secure connection
    app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:H2A0R0I4@localhost/flasknote' #using pymysql for connection to database here flasknote is the database
    db.init_app(app)

    login_manager=LoginManager()
    login_manager.login_view='auth.login' #setting the path to the page to redirect when no user is logged in
    login_manager.init_app(app) #initalizing login manager with the app

    from .views import views
    from .auth import auth


    # registering paths to the main app
    app.register_blueprint(views,url_prefix='/') 
    app.register_blueprint(auth,url_prefix='/')

    from . import model


    #Making tables if table doesn't exist
    with app.app_context():
        db.create_all()
    
    #loading user on reopening browser
    @login_manager.user_loader
    def load_user(id):
        return model.User.query.get(int(id))


    return app


