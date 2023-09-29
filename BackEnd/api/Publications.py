from flask import Blueprint, jsonify, request,json
from config.db import db, app, ma
from models.Publications import Publications, PublicationsSchema

ruta_publications = Blueprint("ruta_publications",__name__)
#routes_cliente = Blueprint("routes_cliente", __name__)

publication_schema = PublicationsSchema()
publications_schema = PublicationsSchema(many=True)

@ruta_publications.route("/publications", methods=["GET"])
def publications():
    resultall = Publications.query.all()
    result = publications_schema.dump(resultall)
    return jsonify(result)

@ruta_publications.route("/savepublication", methods=["POST"])
def savepublication():
    id_com = request.json['id_com']
    id_user = request.json['id_user']
    menssages = request.json['menssage']
    new_publication = Publications(id_com, id_user, menssages)
    db.session.add(new_publication)
    db.session.commit()
    return "Datos guardados con exitos"

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
 
