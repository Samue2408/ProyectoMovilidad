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

def agg_strategicPoints(idBikeway, nombre, descripcion, latitud, longitud, tipo):
    # Verificar si ya existe un registro con el mismo nombre
    punto_existente = StrategicsPoints.query.filter_by(name=nombre).first()
    if punto_existente is None:
        # Si no existe, agrega el nuevo producto
        nuevo_strategicsP = StrategicsPoints(id_bikeway=idBikeway, name=nombre, description=descripcion, longitude=longitud, latitude=latitud, type=tipo)
        db.session.add(nuevo_strategicsP)

with app.app_context():
    db.create_all()

    agg_strategicPoints(1, nombre='colegio la Salle', descripcion='Colegio privado', latitud="10.981932", longitud="-74.787708", tipo= "institucion educativa" )
    agg_strategicPoints(1, nombre='Confamiliar', descripcion='Institucion que ofrece programas de salud, educación, recreación y demás servicios comunitarios.', latitud="11.001483", longitud="-74.816451", tipo= "Caja de Compensación Familiar" )
    
    #p_estrategicos1 = StrategicsPoints(name='Colegio La Salle', description='Colegio Privado', longitude="-74.787708", latitude="10.981932", type="Institucion educatiba")
    db.session.commit()

class StrategicsPointsSchema(ma.Schema):
    class Meta:
        fields = ('id_spoints', 'id_bikeway', 'name', 'description', 'longitude', 'latitude', 'type')