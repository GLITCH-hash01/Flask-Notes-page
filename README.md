# Notes app
---


### Requirements

+ flask
+ flask_sqlalchemy
+ flask_login
+ pymysql
+ cryptography

### Setting up database

1. Make an SQL database named 'flasknote'

2. Replace the username and password in this line
```
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://username:password@localhost/flasknote'
```
