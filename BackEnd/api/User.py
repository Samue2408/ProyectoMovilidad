from flask import Blueprint, jsonify, request,json, redirect, url_for, session
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
    name = request.json['name'].lower()
    email = request.json['email'].lower()
    password = request.json['password']
    genre = request.json['genre']
    user = db.session.query(User.id_user).filter(User.name == name).all()

    result = users_schema.dump(user)

    if len(result)==0:
        user = db.session.query(User.id_user).filter(User.email == email).all()
        result = users_schema.dump(user)

        if len(result) == 0:
            new_user = User(name, email, password, genre)
            db.session.add(new_user)
            db.session.commit()
            return jsonify({'mensaje': 'Registro exitoso'})
        else:
            return jsonify({'error': 'Opss... email en uso'}), 401  
    else:
        return jsonify({'error': 'Opss... nombre en uso'}), 401 
        

@ruta_user.route("/updateuser", methods=["PUT"])
def updateuser():
    id = request.json['id_user'] 
    nuser = User.query.get(id) #Select * from Cliente where id = id
    nuser.name = request.json['name']
    nuser.password = request.json['password']
    session['name'] = request.json['name']
    session['password'] = request.json['password']
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
    user = db.session.query(User.genre, User.id_user, User.name).filter(User.email == email, User.password == password).all()
    
    result = users_schema.dump(user)

    if len(result)>0:
        usuario = result[0]
        session['id_user'] = usuario['id_user']
        session['email'] = email
        session['name'] = usuario['name']
        session['password'] = password
        session['genre'] = usuario['genre']   
        print(session['id_user'])   
        return jsonify({'mensaje': 'Bienvenido'})
    else:
        return jsonify({'error': 'Opss...'}), 401
 