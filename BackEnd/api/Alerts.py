from flask import Blueprint, jsonify, request,json
from config.db import db, app, ma
from models.Alertas import Alerts, AlertSchema

ruta_alerts = Blueprint("ruta_alerts",__name__)
#routes_cliente = Blueprint("routes_cliente", __name__)

alert_schema = AlertSchema()
alerts_schema = AlertSchema(many=True)

@ruta_alerts.route("/alerts", methods=["GET"])
def alerts():
    resultall = Alerts.query.all()
    result = alerts_schema.dump(resultall)
    return jsonify(result)

@ruta_alerts.route("/savealert", methods=["POST"])
def savealert():
    id_bikeway = request.json['id_bikeway']
    id_user = request.json['id_user']
    type = request.json['type']
    description = request.json['description']
    longitude = request.json['longitude']
    latitude = request.json['latitude']
    date_time = request.json['date_time']
    new_alert = Alerts(id_bikeway, id_user, type, description, longitude, latitude, date_time)
    db.session.add(new_alert)
    db.session.commit()
    return "Datos guardados con exitos"

@ruta_alerts.route("/updatealert", methods=["PUT"])
def updatealert():
    id = request.json['id_ale']
    nalert = Alerts.query.get(id) #Select * from Cliente where id = id
    nalert.id_bikeway = request.json['id_bikeway']
    nalert.id_user = request.json['id_user']
    nalert.type = request.json['type']
    nalert.description = request.json['description']
    nalert.longitude = request.json['longitude']
    nalert.latitude = request.json['latitude']
    nalert.date_time = request.json['date_time']
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_alerts.route("/deletealerts/<id>", methods=["GET"])
def deletealerts(id):
    alert = Alerts.query.get(id)
    db.session.delete(alert)
    db.session.commit()
    return jsonify(alert_schema.dump(alert))
 
