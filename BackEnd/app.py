from flask import Flask, redirect, jsonify, render_template, request
from config.db import app

from api.User import ruta_user
from api.Community import ruta_community
from api.Publications import ruta_publications
from api.Usu_Com import ruta_usucom
from api.Strategics_Points import ruta_strategics_points
from api.Routes import ruta_route
from api.BikeWays import ruta_bikeways
from api.Alerts import ruta_alerts
from api.Rutp_Bkway import ruta_RutpBkway

app.register_blueprint(ruta_user, url_prefix="/api")
app.register_blueprint(ruta_community, url_prefix="/api")
app.register_blueprint(ruta_publications, url_prefix="/api")
app.register_blueprint(ruta_usucom, url_prefix="/api")
app.register_blueprint(ruta_route, url_prefix="/api")
app.register_blueprint(ruta_strategics_points, url_prefix="/api")
app.register_blueprint(ruta_bikeways, url_prefix="/api")
app.register_blueprint(ruta_alerts, url_prefix="/api")
app.register_blueprint(ruta_RutpBkway, url_prefix="/api")


@app.route("/")
def index():
    return "hola"

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')