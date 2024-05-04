from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cars(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    manufacturer = db.Column(db.String(30))
    model = db.Column(db.String(30))
    instock = db.Column(db.String(5))
    price = db.Column(db.Double)
    
    def __init__(self, manufacturer, model, instock, price):
        self.manufacturer = manufacturer
        self.model = model
        self.instock = instock
        self.price = price

