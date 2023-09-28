from config.db import app, db, ma

class Community(db.Model):
    __tablename__ = "Community"

    id_com = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

with app.app_context():
    db.create_all()

class CommunitySchema(ma.Schema):
    class Meta:
        fields = ('id_com', 'name')