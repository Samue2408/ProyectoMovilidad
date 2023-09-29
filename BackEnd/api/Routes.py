from flask import Blueprint, jsonify, request,json
from config.db import db, app, ma
from models.Routes import Route, RouteSchema

ruta_route = Blueprint("ruta_route", __name__)

route_schema = RouteSchema()
routes_schema = RouteSchema(many=True)

@ruta_route.route("/route", methods=["GET"])
def routes():
    resultall = Route.query.all()
    result = routes_schema.dump(resultall)
    return jsonify(result)

@ruta_route.route("/saveroute", methods=["POST"])
def saveroute():
    name = request.json['name']
    description = request.json['description']
    initial_latitude = request.json['initial_latitude']
    initial_longitude = request.json['initial_longitude']
    final_latitude = request.json['final_latitude']
    final_longitude = request.json['final_longitude']
    create_date = request.json['create_date']
    id_user = request.json['id_user']
    id_spoints = request.json['id_spoints']
    new_route = Route(name, description, initial_latitude, initial_longitude, final_latitude, final_longitude, create_date, id_user, id_spoints)
    db.session.add(new_route)
    db.session.commit()
    return "Datos guardados con exitos"

@ruta_route.route("/updateroute", methods=["PUT"])
def updateroute():
    id_route = request.json['id_route']    
    nSP = Route.query.get(id_route) #Select * from Cliente where id = id
    nSP.name = request.json['name']
    nSP.description = request.json['description']
    nSP.initial_latitude = request.json['initial_latitude']
    nSP.initial_longitude = request.json['initial_longitude']
    nSP.final_latitude = request.json['final_latitude']
    nSP.final_longitude = request.json['final_longitude']
    nSP.create_date = request.json['create_date']
    nSP.id_user = request.json['id_user']
    nSP.id_spoints = request.json['id_spoints']
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_route.route("/deleteroute/<id_route>", methods=["GET"])
def deleteroute(id_route):
    route = Route.query.get(id_route)
    db.session.delete(route)
    db.session.commit()
    return jsonify(route_schema.dump(route))