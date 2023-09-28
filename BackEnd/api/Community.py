from flask import Blueprint, jsonify, request,json
from config.db import db, app, ma
from models.Community import Community, CommunitySchema

ruta_community = Blueprint("ruta_community",__name__)
#routes_cliente = Blueprint("routes_cliente", __name__)

community_schema = CommunitySchema()
communities_schema = CommunitySchema(many=True)

@ruta_community.route("/communities", methods=["GET"])
def communities():
    resultall = Community.query.all()
    result = communities_schema.dump(resultall)
    return jsonify(result)

@ruta_community.route("/savecommunity", methods=["POST"])
def savecommunity():
    name = request.json['name']
    new_community = Community(name)
    db.session.add(new_community)
    db.session.commit()
    return "Datos guardados con exitos"

@ruta_community.route("/updatecommunity", methods=["PUT"])
def updatecommunity():
    id = request.json['id_com']
    name = request.json['name']
    ncommunity = Community.query.get(id) #Select * from Cliente where id = id
    ncommunity.name = name
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_community.route("/deletecommunity/<id>", methods=["GET"])
def deletecommunity(id):
    community = Community.query.get(id)
    db.session.delete(community)
    db.session.commit()
    return jsonify(community_schema.dump(community))
 
 