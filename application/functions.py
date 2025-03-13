from application.models import IncomeExpense

from application import app, db


def add_test_data():
    with app.app_context():
        # Add some test data
        entry1 = IncomeExpense(type='Income', category='Salary', amount=5000)
        entry2 = IncomeExpense(type='Expense', category='Rent', amount=1000)

        # Add the data to the database
        db.session.add(entry1)
        db.session.add(entry2)

        # Commit the changes
        db.session.commit() 


def review_data():
    with app.app_context():
        # Query the database
        entries = IncomeExpense.query.all()

        # Print the data
        for entry in entries:
            print(entry)