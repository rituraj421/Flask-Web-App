from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
 
app = Flask(__name__)
app.config["SECRET_KEY"] = 'secret-key'
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///data.db'

db = SQLAlchemy(app)
#outside 
@app.before_first_request
def create_tables():
    db.create_all()
#end outside
from routes import *

if __name__ == '__main__':
    app.run(debug=True)