from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.dojo import Dojo


#==========================================================
# Display the base html route
#==========================================================
@app.route('/')
def index():
    dojos = Dojo.get_all_dojos()
    return render_template('/index.html', dojos = dojos)

#==========================================================
# Create a new Dojo
#==========================================================
@app.route('/create_dojo', methods=['POST'])
def create_dojo():
    data = {
        'dname' : request.form['dname']
    }
    Dojo.create_dojo(data)
    return redirect('/')

#==========================================================
# Show one Dojo 
#==========================================================
@app.route('/show_dojo/<int:dojo_id>')
def show_dojo(dojo_id):
    data = {
        'dojo_id' : dojo_id
    }
    dojo = Dojo.get_ninjas_from_dojo(data)
    return render_template('show_ninjas.html', dojo = dojo)
