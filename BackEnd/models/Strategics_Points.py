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
        nuevo_strategicsP = StrategicsPoints(id_bikeway=idBikeway, name=nombre, description=descripcion, latitude=latitud, longitude=longitud, type=tipo)
        db.session.add(nuevo_strategicsP)

with app.app_context():
    db.create_all()

    agg_strategicPoints(idBikeway=1, nombre='colegio la Salle', descripcion='Colegio privado', latitud="10.981932", longitud="-74.787708", tipo= "Institucion educativa" )
    agg_strategicPoints(idBikeway=7, nombre='Confamiliar', descripcion='Ofrece programas de salud, educación, recreación y demás servicios comunitarios.', latitud="11.001483", longitud="-74.816451", tipo= "Caja de Compensación Familiar")
    agg_strategicPoints(idBikeway=7, nombre='Fundecor', descripcion='Fundación privada', latitud="10.999344", longitud="-74.812926", tipo= "Fundación educativa")
    agg_strategicPoints(idBikeway=7, nombre='Gimnacio Universal', descripcion='Ginmacio privado', latitud="10.992399667921989", longitud="-74.7974966573514", tipo= "Centro deportivo" )
    agg_strategicPoints(idBikeway=7, nombre='Cari suri salcedo', descripcion='Comando de Atención Inmediata (CAI)', latitud="10.993928174039482", longitud="-74.80349615467243", tipo= "Unidad policiaca" )
    agg_strategicPoints(idBikeway=7, nombre='Cajero Bancolombia', descripcion='Establecimiento comercial', latitud="10.990592895293043", longitud="-74.786884155670767", tipo= "Patrimonio privado" )
    agg_strategicPoints(idBikeway=1, nombre='Centro materno infantil adelita char', descripcion='Institucion - IPS', latitud="10.96639515164512", longitud="-74.79286949929701", tipo= "Privada")
    agg_strategicPoints(idBikeway=1, nombre='Colegio mayor de barranquilla', descripcion='Colegio privado', latitud="10.985631446039365", longitud="-74.78683369822988", tipo= "Institucion educativa" )
    agg_strategicPoints(idBikeway=1, nombre='Altos de chiquinquirá', descripcion='conjunto residencial', latitud="10.976119411767536", longitud="-74.78917503974864", tipo= "Patrimonio privado" )  
    agg_strategicPoints(idBikeway=2, nombre='clinica la victoria', descripcion='Institucion - IPS', latitud="10.955866453433446", longitud="-74.79486853161218", tipo= "Institucion privada" )
    agg_strategicPoints(idBikeway=8, nombre='Hotel Dorado Plaza Alto Prado', descripcion='Hotel 4 estrellas', latitud="11.003747173285623", longitud="-74.81652935415434", tipo= "Patrimonio privado")
    agg_strategicPoints(idBikeway=8, nombre='Nuestra Señora Del Carmen', descripcion='Colegio privado', latitud="10.99122113068605", longitud="-74.79187344796547", tipo= "Institucion educativa" ) 
    agg_strategicPoints(idBikeway=8, nombre='Parque las americas', descripcion='Zona recreacinal', latitud="10.994096", longitud="-74.797825", tipo= "Zona pública" )
    agg_strategicPoints(idBikeway=3, nombre='Portal de san jose', descripcion='Conjunto residencial', latitud="10.964810", longitud="-74.794404", tipo= "Zona privada")
    agg_strategicPoints(idBikeway=4, nombre='La Fabrica Music Hall', descripcion='Discoteca', latitud="10.964615804357631", longitud="-74.79608674068784", tipo= "Zona privada")
    agg_strategicPoints(idBikeway=5, nombre='Salón Caríbe', descripcion='Salon de toda tipo de evento', latitud="10.985578785308821", longitud="-74.79615440707241", tipo= "Patrimonio privado" )
    agg_strategicPoints(idBikeway=6, nombre='Clinica el prado', descripcion='Intitucion promotora de la salud', latitud="10.991956829808473", longitud="-74.79361489073285", tipo= "Institucion privada" )
    agg_strategicPoints(idBikeway=11, nombre='Diario la Libertad', descripcion='Periódico noticioso de Colombia', latitud="10.992558334356081", longitud="-74.79253187695366", tipo= "Institucion privada")
    agg_strategicPoints(idBikeway=11, nombre='Universidad americana', descripcion='Sede prado', latitud="10.996073664318637", longitud="-74.79699706344863", tipo= "Institucion privada")
    agg_strategicPoints(idBikeway=12, nombre='CLINICA JALLER', descripcion='Hospital de alta complejidad', latitud="10.994043062592628", longitud="-74.7948204505338", tipo= "Institucion privada")
    agg_strategicPoints(idBikeway=13, nombre='CATEDRAL METROPOLITANA', descripcion='Iglesia catolica', latitud="10.988449035536558", longitud="-74.79008288573483", tipo= "Institucion pública")


    #p_estrategicos1 = StrategicsPoints(name='Colegio La Salle', description='Colegio Privado', longitude="-74.787708", latitude="10.981932", type="Institucion educatiba")
    db.session.commit()

class StrategicsPointsSchema(ma.Schema):
    class Meta:
        fields = ('id_spoints', 'id_bikeway', 'name', 'description', 'longitude', 'latitude', 'type')