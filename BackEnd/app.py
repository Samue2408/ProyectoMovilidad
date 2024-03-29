from flask import Flask, redirect, jsonify, render_template, request, session, url_for
from config.db import app, db

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
    if "email" in session:
        return redirect(url_for("principal"))
    else:
        return redirect(url_for("login"))


@app.route("/mapa")
def mapa():
    if "email" in session:
        return render_template("mapa.html")
    else:
        return redirect(url_for("login"))

@app.route("/mapa/<inicial>/<fina>")
def mapa_ciclo(inicial, fina):
    if "email" in session:
        return render_template("mapa.html", initial= inicial, final=fina)
    else:
        return redirect(url_for("login"))

@app.route("/foro")
def comunidad():
    if "communities" in session:
        return render_template("foro.html", comunidades=session['communities'])
    else:
        return redirect(url_for("ruta_community.communities"))


@app.route("/ciclorutas")
def cicloruta():
    if "ciclorutas" in session:
        return render_template("ciclorutas.html", rutas=session["ciclorutas"])
    else:
        return redirect(url_for("ruta_bikeway.bikeways"))


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/principal")
def principal():
    if "email" in session:
        return render_template("index.html", Email=session["email"])
    else:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


def pagina_no_encontrada(error):
    return render_template("404.html"), 404


@app.route("/prueba")
def prueba():
    return render_template("act_info.html", User=session, Email=session["email"])


@app.route("/comunidad/<int:id>")
def comunidad_especifica(id):
    session['id_community_active'] = id
    
    if "publications" in session and id == session['community_active']["id_com"]:
            return render_template(
                "comunidad.html", comunidad=session['community_active'], publicaciones=session['publications'], id_user=session['id_user']
            )
    else:
        return redirect(url_for("ruta_publications.publications"))


@app.route("/crear_comunidad", methods=["GET", "POST"])
def crear_comunidad():
    # Si el método de la solicitud es GET o si hay un error al crear la comunidad, muestra el formulario
    return render_template("crear_comunidad.html", Email=session["email"], User=session)


if __name__ == "__main__":
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True, port=5000, host="0.0.0.0")
