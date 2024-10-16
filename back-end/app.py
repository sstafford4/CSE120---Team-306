# ok so this file MUST be called app.py. thats how flask works.
# import all this stuff. request is for the http requests, render_template is for the html/react, redirect and url_for are obvious
from flask import Flask, request, render_template, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS  # this is for react integration
from config import app, db
from models import Test, Event, fullEvent


# overall list of things to pip install: psycopg2, flask, flask_sqlalchemy
# its also helpful to have the postgres PGAdmin too to visualize the db


# this is the most important part of the process i think
# when the "submit" path is triggered, it gives us access to get and post requests.
# then it takes in the inputted values FROM THE HTML page and sets them as the attibute values.
# notice the names in '' in the request.form statements.
# those names coincide with the names of the input tags in html. NAMES. not ids. Its different, i guess.
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        data = request.json # bc we're using react.js you have to convert all of the data to json
        s_email = data.get('s_email')
        s_name = data.get('s_name')
        s_lang = data.get('s_lang')
        # s_email = request.form['s_email']
        # s_name = request.form['s_name']
        # s_lang = request.form['s_lang']

        # this is where we create an object of type table. It triggers the default constructor and actually sets the attribute values.
        test = Test(s_email, s_name, s_lang)
        db.session.add(test)  # i think this takes everything and adds it to the database.
        db.session.commit()  # this commits the addition to the database
        # return redirect(url_for('index')) # this redirects the page back to the html so that you can enter another name
        return jsonify({'message': 'Data added to table Test'}), 200


# this works perfectly. just change the route and assign a button to it in the html and we can have different things going to different tables in the db.
@app.route('/submit2', methods=['GET', 'POST'])
def submit2():
    if request.method == 'POST':
        data = request.json
        e_month = data.get('e_month')
        e_day = data.get('e_day')
        e_year = data.get('e_year')
        # e_month = request.form['e_month']
        # e_day = request.form['e_day']
        # e_year = request.form['e_year']

        testEvent = Event(e_month, e_day, e_year)
        db.session.add(testEvent)
        db.session.commit()
        # return redirect(url_for('index'))
        return jsonify({'message': 'Data added to table Event'}), 200


# The route for my full demo
@app.route('/submit3', methods=['GET', 'POST'])
def submit3():
    if request.method == 'POST':
        data = request.json
        student_email = data.get('student_email')
        event_date = data.get('event_date')
        event_room = data.get('event_room')
        # student_email = request.form['student_email']
        # event_date = request.form['event_date']
        # event_room = request.form['event_room']

        newEvent = fullEvent(student_email, event_date, event_room)
        db.session.add(newEvent)
        db.session.commit()
        # return redirect(url_for('index'))
        return jsonify({'message': 'Data added to table newEvent'}), 200


# so it doesnt actually make a new table EVERY SINGLE TIME, if the table already exists, it will not make a duplicate.
if __name__ == '__main__':
    with app.app_context():  # this stuff would be what adds the new table. I dont think we will be needing this, but i left it anyway.
        db.create_all()
    app.run(debug=True)  # this runs the flask server

# to run the server, just python app.py in the terminal and then click on the host address and it should open the webpage