from config.db import app, db, ma

class StrategicsPoints(db.Model):
    __tablename__ = "Strategics_Points"

    id_spoints = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    description = db.Column(db.Text)
    longitude = db.Column(db.Text)
    latitude = db.Column(db.Text)
    type = db.Column(db.String(20))

    def __init__(self, name, description, longitude, latitude, type):
        self.name = name
        self.description = description
        self.longitude = longitude
        self.latitude = latitude
        self.type = type

with app.app_context():
    db.create_all()

class StrategicsPointsSchema(ma.Schema):
    class Meta:
        fields = ('id_spoints', 'name', 'description', 'longitude', 'latitude', 'type')