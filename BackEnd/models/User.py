from config.db import app, db, ma
from datetime import date

class User(db.Model):
    __tablename__ = "User"

    id_user = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique= True)
    password = db.Column(db.String(25))
    regis_date = db.Column(db.Date, default=date.today)
    genre = db.Column(db.String(15)) #genero

    def __init__(self, name, email, password, genre):
        self.name = name
        self.email = email
        self.password = password
        self.genre = genre

with app.app_context():
    db.create_all()

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id_user', 'name', 'email', 'password', 'regis_date', 'genre')