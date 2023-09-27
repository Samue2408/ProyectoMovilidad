from flask import Blueprint, jsonify, request,json
from config.db import db, app, ma
from models.Clientes import Clientes, ClienteSchema

ruta_cliente = Blueprint("ruta_cliente",__name__)
#routes_cliente = Blueprint("routes_cliente", __name__)

cliente_schema = ClienteSchema()
clientes_schema = ClienteSchema(many=True)

@ruta_cliente.route("/clientes", methods=["GET"])
def clientes():
    resultall = Clientes.query.all()
    result = clientes_schema.dump(resultall)
    return jsonify(result)

@ruta_cliente.route("/savecliente", methods=["POST"])
def savecliente():
    nombre = request.json['nombre']
    new_cliente = Clientes(nombre)
    db.session.add(new_cliente)
    db.session.commit()
    return "Datos guardados con exitos"

@ruta_cliente.route("/updatecliente", methods=["PUT"])
def updatecliente():
    id = request.json['id']
    nombre = request.json['nombre']
    ncliente = Clientes.query.get(id) #Select * from Cliente where id = id
    ncliente.nombre = nombre
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_cliente.route("/deletecliente/<id>", methods=["GET"])
def deletecliente(id):
    cliente = Clientes.query.get(id)
    db.session.delete(cliente)
    db.session.commit()
    return jsonify(cliente_schema.dump(cliente))
 
 