from config.db import app, db, ma

class Usu_com(db.Model):
    __tablename__ = "Usu_Com"

    id_usuCom = db.Column(db.Integer, primary_key = True)
    id_com = db.Column(db.Integer, db.ForeignKey('Community.id_com'))
    id_user = db.Column(db.Integer, db.ForeignKey('User.id_user'))

    def __init__(self, id_com, id_user):
        self.id_com = id_com
        self.id_user = id_user

with app.app_context():
    db.create_all()

class Usu_comSchema(ma.Schema):
    class Meta:
        fields = ('id_usuCom', 'id_com', 'id_user')