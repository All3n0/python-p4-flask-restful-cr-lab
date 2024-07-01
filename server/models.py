from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()
delete = db.session.delete
class Plant(db.Model, SerializerMixin):
    __tablename__ = 'plants'
    delete = db.session.delete
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    image = db.Column(db.String)
    price = db.Column(db.Float)

    def __repr__(self):
        return f'<Plant {self.name} | Price: {self.price}>'