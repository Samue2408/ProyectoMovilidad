from flask import Blueprint, jsonify, request,json, session, redirect, url_for
from config.db import db, app, ma
from models.Publications import Publications, PublicationsSchema
from models.Community import Community
from api.Community import community_schema
from models.User import User

ruta_publications = Blueprint("ruta_publications",__name__)
#routes_cliente = Blueprint("routes_cliente", __name__)

publication_schema = PublicationsSchema()
publications_schema = PublicationsSchema(many=True)

@ruta_publications.route("/publications", methods=["GET"])
def publications():
    resultall = Publications.query.all()
    result = publications_schema.dump(resultall)
    for resu in result:
        id = User.query.get(resu['id_user'])
        resu['name_user'] = id.name
    session['publications'] = result
    print(result)
    id_com = int(session['id_community_active'])
    ncommunity = Community.query.get(id_com) #Select * from Cliente where id = id
    session['community_active'] = community_schema.dump(ncommunity)
    return redirect(url_for("comunidad_especifica", id=id_com))

@ruta_publications.route("/savepublication", methods=["POST"])
def savepublication():
    id_com = request.json['id_com']
    id_user = request.json['id_user']
    menssages = request.json['menssage']
    new_publication = Publications(id_com, id_user, menssages)
    db.session.add(new_publication)
    db.session.commit()
    return redirect(url_for("ruta_publications.publications"))

@ruta_publications.route("/updatepublication", methods=["PUT"])
def updatepublication():
    id = request.json['id_pub']
    npublication = Publications.query.get(id) #Select * from Cliente where id = id
    npublication.id_com = request.json['id_com']
    npublication.id_user = request.json['id_user']
    npublication.menssages = request.json['menssage']
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_publications.route("/deletepublication/<id>", methods=["GET"])
def deletepublication(id):
    publication = Publications.query.get(id)
    db.session.delete(publication)
    db.session.commit()
    return jsonify(publication_schema.dump(publication))
