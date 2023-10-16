from config.db import app, db, ma

class Bike_ways(db.Model):
    __tablename__ = "BikeWays"

    id_bikeway = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), unique= True)
    description = db.Column(db.Text)
    initial_latitude_longitude = db.Column(db.Text)
    final_latitude_longitude = db.Column(db.Text)

    def __init__(self, name, description, initial_latitude_longitude, final_latitude_longitude):
        self.name = name
        self.description = description
        self.initial_latitude_longitude = initial_latitude_longitude
        self.final_latitude_longitude = final_latitude_longitude


def agregar_producto(nombre, descripcion, inicial_latitud_longitud, final_latitud_longitud):
    # Verificar si ya existe un registro con el mismo nombre
    ciclo_existente = Bike_ways.query.filter_by(name=nombre).first()
    if ciclo_existente is None:
        # Si no existe, agrega el nuevo producto
        nuevo_bikeways = Bike_ways(name=nombre, description=descripcion, initial_latitude_longitude=inicial_latitud_longitud, final_latitude_longitude=final_latitud_longitud)
        db.session.add(nuevo_bikeways)
    

with app.app_context():
    db.create_all()

    agregar_producto("Cicloruta calle 47", "Desde la carrera 22 hasta carrera 45 - doble calzada", "10.965221, -74.793391", "10.986721, -74.786396")
    agregar_producto("Cicloruta calle 44", "Desde la carrera 13C hasta carrera 22 - doble calzada", "10.953448, -74.796259", "10.963858, -74.791397")
    agregar_producto("Cicloruta calle 47b", "Desde la carrera 14 hasta carrera 20 - doble calzada", "10.959026, -74.803732", "10.962798, -74.797332")
    agregar_producto("Cicloruta calle 47d - 47c", "Desde la carrera 20 hasta carrera 22 - doble calzada", "10.963403, -74.797234", "10.965825, -74.794576")
    agregar_producto("Cicloruta calle 59", "Desde la av 11 de noviembre hasta carrera 53 - doble calzada", "10.993707, -74.792838", "10.992929, -74.793318")
    agregar_producto("Cicloruta calle 59(2)", "Desde la carrera 53 hasta carrera 47 - via unica(sentido norte-sur)", "10.992929, -74.793318", "10.991481, -74.794621")  
    agregar_producto("Cicloruta carrera 47 - 50", "Desde la calle 88 hasta via 40  - via unica(sentido norte-sur)", "11.003145, -74.823366", "10.987481, -74.777767")  
    agregar_producto("Cicloruta carrera 50", "Desde la via 40 hasta la calle 91  - via unica(sentido sur-norte)", "10.987693, -74.777786", "11.006802, -74.823957")  
    agregar_producto("Cicloruta calle 54", "Desde la avenida 11 de noviembre hasta la carrera 44b  - via unica(sentido norte-sur)", "10.992669, -74.790290", "10.987253, -74.791579") 
    agregar_producto("Cicloruta calle 55", "Desde la carrera 45 hasta la avenida 11 de noviembre  - via unica(sentido sur-norte)", "10.988374, -74.792032", "10.992896, -74.791093") 
    agregar_producto("Cicloruta carrera 53", "Desde la calle 54 hasta la calle 61  - via unica(sentido sur-norte)", "10.991717, -74.790379", "10.994286, -74.794737") 
    agregar_producto("Cicloruta calle 61", "Desde la carrera 53 hasta la carrera 46  - doble calzada", "10.994315, -74.794831", "10.990696, -74.796318") 
    agregar_producto("Cicloruta carrera 45", "Desde la calle 47 hasta la calle 55  - doble calzada - via unica(sentido sur-norte)", "10.986772, -74.786411", "10.988388, -74.792028") 

    db.session.commit()


class Bike_waySchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'initial_latitude_longitude', 'final_latitude_longitude')