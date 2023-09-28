from config.db import app, db, ma

class Usuario(db.Model):
    __tablename__ = "tblUsuario"

    id_ususario = db.Column(db.Integer, primary_key = True)
    nombre_ususario = db.Column(db.String(50))
    correo_usuario = db.Column(db.String(100))
    contraseña = db.Column(db.String(25))
    fecha_registro = db.Column(db.Date)
    genero = db.Column(db.String(15))

    def __init__(self, nombre_ususario, correo_ususario, contraseña, fecha_registro, genero):
        self.nombre_ususario = nombre_ususario

with app.app_context():
    db.create_all()

class UsarioSchema(ma.Schema):
    class Meta:
        fields = ('id_ususario', 'nombre_ususario')