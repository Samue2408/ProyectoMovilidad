from flask import Blueprint, jsonify, request,json
from config.db import db, app, ma
from models.Community import Community, CommunitySchema

ruta_community = Blueprint("ruta_community",__name__)
#routes_cliente = Blueprint("routes_cliente", __name__)

community_schema = CommunitySchema()
community_schema = CommunitySchema(many=True)

@ruta_community.route("/Community", methods=["GET"])
def community():
    resultall = Community.query.all()# Select * from Ruta;
    result = community_schema.dump(resultall)
    return jsonify(result)


@ruta_community.route("/saveCommunity", methods=["POST"])
def saveCommunity():
    data = request.get_json()
    db.session.add(Community(**data))
    db.session.commit()
    return community_schema.jsonify(Community(**data))


@ruta_community.route("/updateCommunity", methods=["PUT"])
def updateCommunity():
    id = request.json['id_comunidad']
    nombre = nombre.json['nombre']
    nCommunity = Community.query.get(id) #Select * from ruta where id = id
    nCommunity.nombre = nombre
    db.session.commit()
    return "Datos Actualizado con exitos."


@ruta_community.route("/deleteCommunity/<id>", methods=["GET"])
def deleteCommunity(id):
    Community = Community.query.get(id)
    db.session.delete(Community)
    db.session.commit()
    return jsonify(community_schema.dump(Community))




