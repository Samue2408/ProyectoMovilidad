from flask import Blueprint, jsonify, request,json, session, render_template
from config.db import db, app, ma
from models.BikeWays import Bike_ways, Bike_waySchema

ruta_bikeways = Blueprint("ruta_bikeway",__name__)
#routes_cliente = Blueprint("routes_cliente", __name__)

bikeway_schema = Bike_waySchema()
bikeways_schema = Bike_waySchema(many=True)

@ruta_bikeways.route("/bikeways", methods=["GET"])
def bikeways():
    resultall = Bike_ways.query.all()
    result = bikeways_schema.dump(resultall)
    session["ciclorutas"] = result
    return render_template("ciclorutas.html", rutas=session["ciclorutas"])

@ruta_bikeways.route("/savebikeway", methods=["POST"])
def savebikeway():
    name = request.json['name']
    description = request.json['description']
    initial_latitude_longitude = request.json['initial_latitude_longitude']
    final_latitude_longitude = request.json['final_latitude_longitude']
    new_bikeway = Bike_ways(name, description, initial_latitude_longitude, final_latitude_longitude)
    db.session.add(new_bikeway)
    db.session.commit()
    return "Datos guardados con exitos"

@ruta_bikeways.route("/updatebikeway", methods=["PUT"])
def updatebikeway():
    id = request.json['id_bikeway']
    nbikeway = Bike_ways.query.get(id) #Select * from Cliente where id = id
    nbikeway.name = request.json['name']
    nbikeway.description = request.json['description']
    nbikeway.initial_latitude_longitude = request.json['initial_latitude_longitude']
    nbikeway.final_latitude_longitude = request.json['final_latitude_longitude']
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_bikeways.route("/deletebikeway/<id>", methods=["GET"])
def deletebikeway(id):
    bikeway = Bike_ways.query.get(id)
    db.session.delete(bikeway)
    db.session.commit()
    return jsonify(bikeway_schema.dump(bikeway))
 
 