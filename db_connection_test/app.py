# ok so this file MUST be called app.py. thats how flask works. 
#import all this stuff. request is for the http requests, render_template is for the html/react, redirect and url_for are obvious
from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# overall list of things to pip install: psycopg2, flask, flask_sqlalchemy
# its also helpful to have the postgres PGAdmin too to visualize the db

app = Flask(__name__) #this initializes the flask i think? 

# these are the links to the db. postgresql://<user>:<password>@<host>/<database_name>
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12263899@localhost/polyglot'
db = SQLAlchemy(app)

# this is to create a table in the db. it ofc has the id key, then you can make however many more you need.
# thats ALL this does. I dont think that we would normally need this. 
class Test(db.Model):
    __tablename__ = 'test'
    # these are the attributes of the table
    id = db.Column(db.Integer, primary_key=True)
    s_email = db.Column(db.String(100))
    s_name = db.Column(db.String(100))
    s_lang = db.Column(db.String(40))

    # this the default constructor of the class
    def __init__(self,s_email, s_name, s_lang):
        self.s_email = s_email
        self.s_name = s_name
        self.s_lang = s_lang

#this is what renders the html file. 
@app.route('/')
def index():
    return render_template('index.html') # change this to whatever react file or whatever we would use
# ALSO: all html files need to be in the template folder, thats where flask looks to see if they exist. 

# this is the most important part of the process i think
# when the "submit" path is triggered, it gives us access to get and post requests. 
# then it takes in the inputted values FROM THE HTML page and sets them as the attibute values.
# notice the names in '' in the request.form statements.
# those names coincide with the names of the input tags in html. NAMES. not ids. Its different, i guess.
@app.route('/submit', methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        s_email = request.form['s_email']
        s_name = request.form['s_name']
        s_lang = request.form['s_lang']

        # this is where we create an object of type table. It triggers the default constructor and actually sets the attribute values.
        test = Test(s_email, s_name, s_lang)
        db.session.add(test) # i think this takes everything and adds it to the database.
        db.session.commit() # this commits the addition to the database
        return redirect(url_for('index')) # this redirects the page back to the html so that you can enter another name

if __name__ == '__main__':
    # with app.app_context(): # this stuff would be what adds the new table. I dont think we will be needing this, but i left it anyway. 
    #     db.create_all()
    app.run(debug=True) # this runs the flask server
    
# to run the server, just python app.py in the terminal and then click on the host address and it should open the webpage
