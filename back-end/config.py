from flask import Flask, request, render_template, url_for
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) #this initializes the flask i think?
CORS(app) #this is working in pycharm for me, use the other one in VSCode
#CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})# this would allow for integration with a React app, as theyre both hosted on different ports
# Flask is hosted on port 5000, React is hosted on port 3000

# these are the links to the db. postgresql://<user>:<password>@<host>/<database_name>
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12263899@localhost/polyglot'
db = SQLAlchemy(app)
