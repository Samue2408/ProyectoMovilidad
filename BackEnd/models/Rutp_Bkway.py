from config.db import app, db, ma

class Rutp_Bkway(db.Model):
    __tablename__ = "Rutp_Bkway"

    id_RutpBkway = db.Column(db.Integer, primary_key = True)
    id_route = db.Column(db.Integer, db.ForeignKey('Routes.id_route'))
    id_bikeway = db.Column(db.Integer, db.ForeignKey('BikeWays.id_bikeway'))

    def __init__(self, id_route, id_bikeway):
        self.id_route = id_route
        self.id_bikeway = id_bikeway

with app.app_context():
    db.create_all()

class RutpBkwaySchema(ma.Schema):
    class Meta:
        fields = ('id_RutpBkway', 'id_route', 'id_bikeway')