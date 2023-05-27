from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db=SQLAlchemy()
dbname='database.db'


def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY'] ='hkjadkfasdfasdfasdfasdfasdfasdfasdfasdfasdf'
    app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:H2A0R0I4@localhost/flasknote'
    db.init_app(app)

    login_manager=LoginManager()
    login_manager.login_view='auth.login'
    login_manager.init_app(app)




    from .views import views
    from .auth import auth

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')

    from . import model

    with app.app_context():
        db.create_all()
    
    @login_manager.user_loader
    def load_user(id):
        return model.User.query.get(int(id))







    return app


