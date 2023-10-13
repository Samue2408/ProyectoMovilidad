from flask import Blueprint, jsonify, request,json, redirect, url_for
from config.db import db, app, ma
from models.User import User, UserSchema

ruta_user = Blueprint("ruta_user",__name__)


user_schema = UserSchema()
users_schema = UserSchema(many=True)

@ruta_user.route("/user", methods=["GET"])
def users():
    resultall = User.query.all()
    result = users_schema.dump(resultall)
    return jsonify(result)

@ruta_user.route("/saveuser", methods=["POST"])
def saveuser():
    name = request.json['name']
    email = request.json['email']
    password = request.json['password']
    genre = request.json['genre']
    new_user = User(name, email, password, genre)
    db.session.add(new_user)
    db.session.commit()
    return "Datos guardados exitosamente"

@ruta_user.route("/updateuser", methods=["PUT"])
def updateuser():
    id = request.json['id_user']    
    nuser = User.query.get(id) #Select * from Cliente where id = id
    nuser.name = request.json['name']
    nuser.email = request.json['email']
    nuser.password = request.json['password']
    nuser.genre = request.json['genre']
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_user.route("/deleteuser/<id>", methods=["GET"])
def deleteusuario(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify(user_schema.dump(user))

@ruta_user.route("/signin", methods=["POST"])
def signin():
    email = request.json['email']
    password = request.json['password']
    user = db.session.query(User.id_user).filter(User.email == email, User.password == password).all()

    result = users_schema.dump(user)

    if len(result)>0:
        return jsonify({'mensaje': 'Inicio de sesión exitoso'})
    else:
        return jsonify({'error': 'Credenciales incorrectas'}), 401
 