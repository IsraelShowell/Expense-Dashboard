from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SelectField, SubmitField
from wtforms.validators import DataRequired



class UserInputForm(FlaskForm):
    #This is a selection field that allows the user to select the type of transaction
    #The choices are either Income or Expense
    #The choices are stored in a tuple, where the first value is the value that is stored in the database
    #and the second value is the value that is displayed to the user

    type = SelectField('Type', validators=[DataRequired()], choices=[('Income', 'Income'), ('Expense', 'Expense')])

    category = SelectField('Category', validators=[DataRequired()], choices=[('rent', 'rent'), ('salary', 'salary'), ('investment', 'investment'), ('other', 'other')])

    amount = IntegerField('Amount', validators=[DataRequired()])

    submit = SubmitField('Generate Report')