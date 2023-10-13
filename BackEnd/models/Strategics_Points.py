from config.db import app, db, ma

class StrategicsPoints(db.Model):
    __tablename__ = "Strategics_Points"

    id_spoints = db.Column(db.Integer, primary_key = True)
    id_bikeway = db.Column(db.Integer, db.ForeignKey('BikeWays.id_bikeway'))
    name = db.Column(db.String(50))
    description = db.Column(db.Text)
    longitude = db.Column(db.Text)
    latitude = db.Column(db.Text)
    type = db.Column(db.String(20))

    def __init__(self, id_bikeway,  name, description, longitude, latitude, type):
        self.id_bikeway = id_bikeway
        self.name = name
        self.description = description
        self.longitude = longitude
        self.latitude = latitude
        self.type = type

with app.app_context():
    db.create_all()
    #p_estrategicos1 = StrategicsPoints(name='Colegio La Salle', description='Colegio Privado', longitude="-74.787708", latitude="10.981932", type="Institucion educatiba")

class StrategicsPointsSchema(ma.Schema):
    class Meta:
        fields = ('id_spoints', 'id_bikeway', 'name', 'description', 'longitude', 'latitude', 'type')