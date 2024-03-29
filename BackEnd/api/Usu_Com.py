from flask import Blueprint, jsonify, request,json
from config.db import db, app, ma
from models.Usu_Com import Usu_com, Usu_comSchema
from models.Community import Community
from api.Community import communities_schema

ruta_usucom = Blueprint("ruta_usucom",__name__)
#routes_cliente = Blueprint("routes_cliente", __name__)

usucom_schema = Usu_comSchema()
usucoms_schema = Usu_comSchema(many=True)

@ruta_usucom.route("/usucoms", methods=["GET"])
def usucoms():
    resultall = usucoms.query.all()
    result = usucoms_schema.dump(resultall)
    return jsonify(result)

@ruta_usucom.route("/saveusucom", methods=["POST"])
def saveusucom():
    name_com = request.json['name']
    comm = db.session.query(Community.id_com, Community.name).filter(Community.name == name_com).all()
    print(comm)

    result = communities_schema.dump(comm)
    
    if len(result) > 0 : 
        usu_coms =result[0]       
        id_comm = usu_coms['id_com']
        id_user = request.json['id_user']
        type_usu = request.json['type_usu']
        new_usucom = Usu_com(id_comm, id_user, type_usu)
        db.session.add(new_usucom)
        db.session.commit()   
        return jsonify({'mensaje': 'Comunidad Creada'})

@ruta_usucom.route("/updateusucom", methods=["PUT"])
def updateusucom():
    id = request.json['id_usuCom']
    nusucom = Usu_com.query.get(id) #Select * from Cliente where id = id
    nusucom.id_com = request.json['id_com']
    nusucom.id_user = request.json['id_user']
    nusucom.type_usu = request.json['type_usu']
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_usucom.route("/deleteusucom/<id>", methods=["GET"])
def deleteusucom(id):
    usu_com = Usu_com.query.get(id)
    db.session.delete(usu_com)
    db.session.commit()
    return jsonify(usucom_schema.dump(usu_com))