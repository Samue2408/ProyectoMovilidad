from flask import Blueprint, jsonify, request,json
from config.db import db, app, ma
from models.Rutp_Bkway import Rutp_Bkway, RutpBkwaySchema

ruta_RutpBkway = Blueprint("ruta_rutpbkway",__name__)


Rutpbkway_schema = RutpBkwaySchema()
Rutpbkways_schema = RutpBkwaySchema(many=True)

@ruta_RutpBkway.route("/Rutp_Bkway", methods=["GET"])
def Rutp_Bkway():
    resultall = Rutp_Bkway.query.all()
    result = Rutpbkways_schema.dump(resultall)
    return jsonify(result)

@ruta_RutpBkway.route("/saverutpbkway", methods=["POST"])
def saverutpbkway():
    id_route = request.json['id_route']
    id_bikeway = request.json['id_bikeway']
    new_rutpsbkway = Rutp_Bkway(id_route, id_bikeway)
    db.session.add(new_rutpsbkway)
    db.session.commit()
    return "Datos guardados con exitos"

@ruta_RutpBkway.route("/updaterutpbkway", methods=["PUT"])
def updateusucom():
    id = request.json['id_RutpBkway']
    nusucom = Usu_com.query.get(id) #Select * from Cliente where id = id
    nusucom.id_route = request.json['id_route']
    nusucom.id_bikeway = request.json['id_bikeway']
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_RutpBkway.route("/deleteusucom/<id>", methods=["GET"])
def deleteusucom(id):
    usu_com = Usu_com.query.get(id)
    db.session.delete(usu_com)
    db.session.commit()
    return jsonify(usucom_schema.dump(usu_com))