from application import db
from datetime import datetime

class IncomeExpense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), default = 'Income', nullable=False)
    category = db.Column(db.String(100), default = 'rent', nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.now)

    def __repr__(self):
        return f"IncomeExpense('{self.type}', '{self.category}', '{self.amount}', '{self.date}')"