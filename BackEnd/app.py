from flask import Flask, redirect, jsonify, render_template, request
from config.db import app

from api.User import ruta_user
from api.Community import ruta_community
from api.Publications import ruta_publications

app.register_blueprint(ruta_user, url_prefix="/api")
app.register_blueprint(ruta_community, url_prefix="/api")
app.register_blueprint(ruta_publications, url_prefix="/api")

@app.route("/")
def index():
    return "hola"

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')