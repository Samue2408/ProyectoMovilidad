from config.db import app, db, ma

class Publications(db.Model):
    __tablename__ = "Publicacion"

    id_pub = db.Column(db.Integer, primary_key = True)
    id_com = db.Column(db.Integer, db.ForeignKey('Community.id_com'))
    id_user = db.Column(db.Integer, db.ForeignKey('User.id_user'))
    menssages = db.Column(db.Text)

    def __init__(self, id_com, id_user, menssages):
        self.id_com = id_com
        self.id_user = id_user
        self.menssages = menssages

with app.app_context():
    db.create_all()

class PublicationsSchema(ma.Schema):
    class Meta:
        fields = ('id_pub', 'id_com', 'id_user', 'menssages')