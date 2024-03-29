from config.db import app, db, ma

class Route(db.Model):
    __tablename__ = "Routes"
     
    id_route = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(50))
    latitude_inicial = db.Column(db.String(50))
    latitude_final = db.Column(db.String(50))
    longitude_inicial = db.Column(db.String(50))
    longitude_final = db.Column(db.String(50))
    create_date = db.Column(db.String(50))
    id_spoints = db.Column(db.Integer, db.ForeignKey('Strategics_Points.id_spoints'))
    id_user = db.Column(db.Integer, db.ForeignKey('User.id_user'))
    
    def __init__(self, name, description, initial_latitude, initial_longitude, final_latitude, final_longitude, create_date, id_user, id_spoints):
        self.name = name
        self.description = description
        self.initial_latitude = initial_latitude
        self.initial_longitude = initial_longitude
        self.final_latitude = final_latitude
        self.final_longitude = final_longitude
        self.create_date = create_date
        self.id_user = id_user
        self.id_spoints = id_spoints
        
with app.app_context():
    db.create_all()

class RouteSchema(ma.Schema):
    class Meta:
        fields = ('id_route', 
                  'name', 'description', 'initial_latitude', 
                  'initial_longitude', 'final_latitude', 
                  'final_longitude','create_date', 'id_user', 'id_spoints')