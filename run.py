#Run this file to start the application
#If you are using a virtual environment, make sure to activate it before running this file.

from application import app, db

from application.models import IncomeExpense

from application.functions import add_test_data, review_data



def create_database():
    with app.app_context():  # Ensures an application context is active
        db.create_all()  # Create all SQL tables



if __name__ == "__main__":
    create_database()
    #add_test_data()
    #review_data()

    app.run(debug=True)