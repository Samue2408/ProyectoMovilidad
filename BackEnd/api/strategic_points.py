from flask import request, jsonify, json, Blueprint
from config.db import app, ma, db
from models.strategic_points import strategic_points,strategic_pointSchema

ruta_strategicPoints = Blueprint("ruta_strategicPoints", __name__)

Strategic_PointSchema = strategic_pointSchema()
Strategic_PointSchema = strategic_pointSchema(many=True)

@ruta_strategicPoints.route("/strategicPoints", methods=["GET"])
def StrategicPoints():
    resultall = strategic_points.query.all()
    result = strategic_pointSchema.dump(resultall)
    return jsonify(result)

@ruta_strategicPoints.route("/savestrategicPoints", methods=["POST"])
def savestrategic_points():
    
    new_StrategicPoints = strategic_points (
        name = request.json['name'],
        description = request.json['description'],
        latitude = request.json['dlatitude'],
        longitude = request.json['longitude'],
        coments = request.json['coments'],
        type = request.json['type']
    )
    db.session.add(new_StrategicPoints)
    db.session.commit()
    return "Datos guardados con exitos"

@ruta_strategicPoints.route("/updateStrategicPoints", methods=["PUT"])
def updateStrategicPoints():
    id_spoints = request.json['id_spoints']
    name = request.json['name']
    description = request.json['description']
    latitude = request.json['latitude']
    longitude = request.json['longitude']
    coments = request.json['coments']
    type = request.json['type']
    nstrategicPoints = strategic_points.query.get(id_spoints) #Select * from Cliente where id = id
    nstrategicPoints.name = name
    nstrategicPoints.description = description
    nstrategicPoints.latitude = latitude
    nstrategicPoints.longitude = longitude
    nstrategicPoints.coments= coments
    nstrategicPoints.type = type
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_strategicPoints.route("/deleteStrategicSpoints/<id_spoints>", methods=["GET"])
def deletecliente(id_spoints):
    Strategic_Poitns = strategic_points.query.get(id_spoints) 
    db.session.delete(Strategic_Poitns)
    db.session.commit()
    return jsonify(strategic_pointSchema.dump(Strategic_Poitns))