from config.db import app, db, ma

class Bike_ways(db.Model):
    __tablename__ = "BikeWays"

    id_bikeway = db.Column(db.Integer, primary_key = True)
    id_spoints = db.Column(db.Integer, db.ForeignKey('Strategics_Points.id_spoints'))
    name = db.Column(db.String(50))
    description = db.Column(db.Text)
    initial_latitude_longitude = db.Column(db.Text)
    final_latitude_longitude = db.Column(db.Text)

    def __init__(self, id_spoints, name, description, initial_latitude_longitude, final_latitude_longitude):
        self.id_spoints = id_spoints
        self.name = name
        self.description = description
        self.initial_latitude_longitude = initial_latitude_longitude
        self.final_latitude_longitude = final_latitude_longitude
    
    """def __init__(self, name, description, initial_latitude_longitude, final_latitude_longitude):
        self.name = name
        self.description = description
        self.initial_latitude_longitude = initial_latitude_longitude
        self.final_latitude_longitude = final_latitude_longitude"""

with app.app_context():
    db.create_all()

class Bike_waySchema(ma.Schema):
    class Meta:
        #fields = ('id','name', 'description', 'initial_latitude_longitude', 'final_latitude_longitude')
        fields = ('id', 'id_spoints', 'name', 'description', 'initial_latitude_longitude', 'final_latitude_longitude')