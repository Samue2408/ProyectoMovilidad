from flask import Blueprint, jsonify, request,json, session, redirect, url_for
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
    session['communities'] = result
    return redirect(url_for("comunidad"))

@ruta_community.route("/savecommunity", methods=["POST"])
def savecommunity():
    name = request.json['name']   
    commu = db.session.query(Community.id_com).filter(Community.name == name).all()
    result = communities_schema.dump(commu)

    if len(result) == 0 :
        new_community = Community(name)    
        db.session.add(new_community)
        db.session.commit()
        resultall = Community.query.all()
        result = communities_schema.dump(resultall)
        session['communities'] = result
        return jsonify({'mensaje': 'Bienvenido'})

    else:
        return jsonify({'error': 'Opss... nombre en uso'}), 401

    

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
 
 