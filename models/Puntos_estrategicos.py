from config.db import app, db, ma

class Puntos_estrategicos(db.Model):
    __tablename__ = "tblptos_Estrategicos"

id_PuntoE = db.Column(db.Integer, primary_key = True)
Descripcion_Punto = db.column(db.String (1000))
Nombre_Punto = db.column(db.String (1000))
Longitud = db.column(db.Float (1000))
Longitud = db.column(db.Float (1000))
Comentarios = db.column(db.String (1000))
Tipo_punto = db.column(db.String (1000))

def __init__(self, id_PuntoE):
    self.id_PuntoE = id_PuntoE

with app.app_context():
    db.create_all()

class Puntos_estrategicosSchema(ma.Schema):
    class Meta:
        fields = ('id_PuntoE', 'Descripcion_Punto', 'Nombre_Punto', 'Longitud', 'Latitud', 'Comentarios', 'Tipo_punto')