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
    return render_template('mapa.html')

@app.route("/foro")
def comunidad():
    return render_template('foro.html')

@app.route("/ciclorutas")
def cicloruta():
    return render_template('ciclorutas.html')

@app.route("/login")
def login():
    return render_template('login.html')
    
@app.route("/principal")
def principal():
    return render_template('index.html', Email= session['email'])

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('login'))

# Ruta para mostrar el perfil del usuario
@app.route('/perfil_usuario/<int:user_id>', methods=['GET', 'POST'])
def perfil_usuario(user_id):
    conn = app.connect('mi_base_de_datos.db')
    cursor = conn.cursor()

    if request.method == 'POST':
        nuevo_nombre = request.form['nombre']
        nueva_contrasena = request.form['contrasena']

        # Actualizar el nombre y la contraseña en la base de datos
        cursor.execute("UPDATE usuarios SET nombre = ?, contrasena = ? WHERE id = ?",
            (nuevo_nombre, nueva_contrasena, user_id))
        conn.commit()

    cursor.execute("SELECT nombre, correo, fecha_ingreso, genero FROM usuarios WHERE id = ?", (user_id,))
    user_info = cursor.fetchone()

    conn.close()

    return render_template('perfil_usuario.html', user_info=user_info)

@app.route("/prueba")
def prueba():
    return render_template('Act_nombre.html')

def pagina_no_encontrada(error):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.register_error_handler(404,pagina_no_encontrada)
    app.run(debug=True, port=5000, host='0.0.0.0')
    app.run(debug=True)
    
    