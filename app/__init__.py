from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from .config import configuracion
from .modelo import Usuario

from ext import db, login_manager, migrate

login_manager.login_view = "auth.login"


def crear_app(nombre_config):
    app = Flask(__name__)
    app.config.from_object(configuracion[nombre_config])
    configuracion[nombre_config].init_app(app)

    # inicializa extensiones
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    @login_manager.user_loader
    def load_user(user_id):
        return Usuario.query.get(int(user_id))

    from .api import api_bp
    from .auth import auth_bp
    from .prin import prin_bp
    from .gral import gral_bp

    app.register_blueprint(api_bp, url_prefix="/api")
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(prin_bp, url_prefix="/principal")
    app.register_blueprint(gral_bp)

    return app
