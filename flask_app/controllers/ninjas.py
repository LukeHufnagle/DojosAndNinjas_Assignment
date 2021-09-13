from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

#=======================================
# Route to add new ninja page
#=======================================
@app.route('/add_ninja')
def show_ninjas():
    dojos = Dojo.get_all_dojos()
    return render_template('add_a_ninja.html', dojos= dojos)

#=======================================
# Create a new ninja
#=======================================
@app.route('/create_ninja', methods=['POST'])
def create_ninja():
    data = {
        'fname' : request.form['fname'],
        'lname' : request.form['lname'],
        'age' : request.form['age'],
        'dojo_id' : request.form['dojo_id']
    }
    Ninja.create_ninja(data)
    return redirect('/')

@app.route('/show_ninjas/<id>')
def show_ninjas_from_dojo(dojo_id):
    data = {
        'dojo_id' : dojo_id
    }
    ninjas = Ninja.get_ninjas_from_dojo(data)
    return render_template('show_ninjas/<id>.html', ninjas = ninjas)