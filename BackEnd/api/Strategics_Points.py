from flask import Blueprint, jsonify, request,json
from config.db import db, app, ma
from models.Strategics_Points import StrategicsPoints, StrategicsPointsSchema

ruta_strategics_points = Blueprint("ruta_strategics_points",__name__)
#routes_cliente = Blueprint("routes_cliente", __name__)

strategic_point_schema = StrategicsPointsSchema()
strategics_points_schema = StrategicsPointsSchema(many=True)

@ruta_strategics_points.route("/strategics_points", methods=["GET"])
def strategics_points():
    resultall = StrategicsPoints.query.all()
    result = strategics_points_schema.dump(resultall)
    return jsonify(result)

@ruta_strategics_points.route("/save_strategics_points", methods=["POST"])
def save_strategics_points():
    name = request.json['name']
    description = request.json['description']
    longitude = request.json['longitude']
    latitude = request.json['latitude']
    type = request.json['type']
    new_strategics_points = StrategicsPoints(name, description, longitude, latitude, type)
    db.session.add(new_strategics_points)
    db.session.commit()
    return "Datos guardados con exitos"

@ruta_strategics_points.route("/update_strategics_points", methods=["PUT"])
def update_strategics_points():
    id = request.json['id_spoints']
    nstrategics_points = StrategicsPoints.query.get(id) #Select * from Cliente where id = id
    nstrategics_points.name = request.json['name']
    nstrategics_points.description = request.json['description']
    nstrategics_points.longitude = request.json['longitude']
    nstrategics_points.latitude = request.json['latitude']
    nstrategics_points.type = request.json['type']
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_strategics_points.route("/delete_strategics_points/<id>", methods=["GET"])
def delete_strategics_points(id):
    strategics_points = StrategicsPoints.query.get(id)
    db.session.delete(strategics_points)
    db.session.commit()
    return jsonify(strategic_point_schema.dump(strategics_points))