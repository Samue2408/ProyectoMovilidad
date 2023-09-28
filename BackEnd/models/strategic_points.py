from config.db import app, db, ma

class strategic_points(db.Model):
    __tablename__ = "tblStrategic_Points"
    
    id_spoints = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(250))
    description = db.column(db.String(250))
    latitude = db.column(db.String(250))
    longitude = db.column(db.String(250))
    coments = db.column(db.String(250))
    type = db.column(db.String(250))

    def __init__(self, name, description, longitude, latitude, coments, type):
        self.name = name
        self.description = description
        self.longitude = longitude
        self.latitude = latitude
        self.coments = coments
        self.type = type
        
with app.app_context():
    db.create_all

class strategic_pointSchema(ma.Schema):
    class Meta:
        fields = ["id", "name", "description", "latitude", "longitude", "coments", "type"]
    
