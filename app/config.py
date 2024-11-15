import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Configuracion:
    SERVER_NAME = os.getenv(f"SERVIDOR")
    SECRET_KEY = os.getenv(f"CLAVE_SECRETA") or f"pr0gr4m4t1c4"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECURITY_PASSWORD_SALT = os.getenv(f"CLAVE_SALT") or f"pr0gr4m4t1c4"
    TEMPLATE_FOLDER = f"/templates"
    STATIC_FOLDER = f"/static"
    MEDICARE_LINEAS_POR_PAGINA = 10

    @classmethod
    def init_app(cls, app):
        pass


class ConfiguracionDesarrollo(Configuracion):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv(f"BASE_DATOS_DES") or f"sqlite:///bdmedicare.db"


class ConfiguracionProduccion(Configuracion):
    SQLALCHEMY_DATABASE_URI = os.getenv(f"BASE_DATOS_PROD")


class ConfiguracionTesteo(Configuracion):
    SQLALCHEMY_DATABASE_URI = os.getenv(
        f"BASE_DATOS_TEST"
    ) or f"sqlite:///" + os.path.join(basedir, "data-des.sqlite")


configuracion = {
    "desarrollo": ConfiguracionDesarrollo,
    "testeo": ConfiguracionTesteo,
    "produccion": ConfiguracionProduccion,
    "defecto": ConfiguracionDesarrollo,
}
