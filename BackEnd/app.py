from flask import Flask, redirect, jsonify, render_template, request, session, url_for
from config.db import app

from api.User import ruta_user
from api.Community import ruta_community
from api.Publications import ruta_publications
from api.Usu_Com import ruta_usucom
from api.BikeWays import ruta_bikeways
from api.Strategics_Points import ruta_strategics_points
from api.Routes import ruta_route
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
    if 'email' in session:
        return redirect(url_for('principal'))
    else:
        return redirect(url_for('login'))

@app.route("/mapa")
def mapa():
    if 'email' in session:
        return render_template('mapa.html', Email= session['email'])
    else:
        return redirect(url_for('login'))

@app.route("/foro")
def comunidad():
    if 'email' in session:
        return render_template('foro.html', Email= session['email'])
    else:
        return redirect(url_for('login'))
    

@app.route("/ciclorutas")
def cicloruta():
    if 'email' in session:
        return render_template('ciclorutas.html', Email= session['email'])
    else:
        return redirect(url_for('login'))

@app.route("/login")
def login():
    return render_template('login.html')
    
@app.route("/principal")
def principal():
    if 'email' in session:
        return render_template('index.html', Email= session['email'])
    else:
        return redirect(url_for('login'))

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('login'))

def pagina_no_encontrada(error):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.register_error_handler(404,pagina_no_encontrada)
    app.run(debug=True, port=5000, host='0.0.0.0')