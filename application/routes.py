from application import app, db
from flask import render_template, flash, redirect, url_for, get_flashed_messages
from application.form import UserInputForm
from application.models import IncomeExpense


#Root route
@app.route("/")
def index():
    #This query retrieves all the entries in the database and orders them by date in descending order
    #This gives the most recent entries first
    entries = IncomeExpense.query.order_by(IncomeExpense.date.desc()).all()

    return render_template("index.html", title="Home", entries = entries)



@app.route("/add", methods = ["GET", "POST"])
def add_expense():

    #Create a form object
    form = UserInputForm()


    #Checks if the form has been submitted and if the data entered is valid
    if form.validate_on_submit():
        #Create a new entry in the database based on the form data
        entry = IncomeExpense(type=form.type.data, category=form.category.data, amount=form.amount.data)
        db.session.add(entry)
        db.session.commit()
        flash('Transaction added successfully', 'success')
        return redirect(url_for('index'))

    return render_template("add.html", title="Add", form = form)


@app.route("/delete/<int:id>")
def delete(id):
    
    #Query the database to get the entry with the specified id
    entry = IncomeExpense.query.get(id)

    #If the entry exists, delete it
    if entry:
        db.session.delete(entry)
        db.session.commit()
        flash('Transaction deleted successfully', 'success')
    else:
        flash('Transaction not found', 'danger')

    return redirect(url_for('index'))