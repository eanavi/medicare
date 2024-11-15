import os
from dotenv import load_dotenv

ruta_env = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(ruta_env):
    load_dotenv(ruta_env)

from flask_migrate import Migrate, upgrade, downgrade
from app import crear_app, db

app = crear_app(os.getenv("CONFIGURACION_FLASK") or "defecto")
migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run()
