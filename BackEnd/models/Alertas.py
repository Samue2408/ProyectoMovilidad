from config.db import app, db, ma
from datetime import datetime

class Alerts(db.Model):
    __tablename__ = "Alerts"

    id_ale = db.Column(db.Integer, primary_key = True)
    id_bikeway = db.Column(db.Integer, db.ForeignKey('BikeWays.id_bikeway'))
    id_user = db.Column(db.Integer, db.ForeignKey('User.id_user'))
    type = db.Column(db.String(20))
    description = db.Column(db.Text)
    longitude = db.Column(db.Text)
    latitude = db.Column(db.Text)
    date_time = db.Column(db.DateTime, default=datetime.utcnow) #si no se proporciona un valor para esta columna al crear un nuevo registro, se utilizará la fecha y hora actual como valor predeterminado

    def __init__(self, id_bikeway, id_user, type, description, longitude, latitude, date_time):
        self.id_bikeway = id_bikeway
        self.id_user = id_user
        self.type = type
        self.description = description
        self.longitude = longitude
        self.latitude = latitude
        self.date_time = date_time

with app.app_context():
    db.create_all()

class AlertSchema(ma.Schema):
    class Meta:
        fields = ('id_ale', 'id_bikeway', 'id_user', 'type', 'description', 'longitude', 'latitude', 'date_time')