# Importando la clase Flask
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# creando extensión de la base de datos
db = SQLAlchemy()

# Creando función de control
def create_app():

    # Creando la variable de iniciación
    app = Flask(__name__)

    # Configuración del proyecto
    app.config.from_mapping(
        DEBUG = True,
        SECRET_KEY='dev_esit',
        SQLALCHEMY_DATABASE_URI = "sqlite:///todolist.db"
    )

    # iniciando conexion
    db.init_app(app)

    # Registrando Blueprint
    from . import todo
    app.register_blueprint(todo.bp)

    from . import auth
    app.register_blueprint(auth.bp)

    # Definiendo rutas
    @app.route('/')
    def index():
        return render_template('index.html')

    #creación de tablas a partir de los modelos
    with app.app_context():
        db.create_all()    

    return app