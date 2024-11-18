from flask import render_template, session
from flask_login import login_required
from sqlalchemy import desc
from app import db
from app.modelo import Persona, Acceso
from . import prin_bp


@prin_bp.route("/iniciodash/<string:tipo>")
@login_required
def iniciodash(tipo):

    titulo = ""
    titulo2 = ""
    ultimas_personas = []
    rutas = []

    te = session.get("tipo_empleado", "I")

    rutas = (
        Acceso.query.where(Acceso.tipo_usuario == te).order_by(Acceso.id_acceso).all()
    )

    if len(tipo) <= 2:
        titulo2 = rutas[0].nombre_acceso.capitalize() if rutas else "Personas"
    else:
        titulo2 = tipo.capitalize()

    titulo = te

    return render_template(
        "prin/dashboard.html",
        datos=[],
        acc=rutas,
        t1=titulo,
        tipoPersona=titulo2,
    )


@prin_bp.route("/dashboard/<string:tipo>")
@login_required
def dashboard(tipo):

    titulo2 = ""

    ultimas_personas = []
    rutas = []

    if tipo == "M":  # Medicos
        titulo2 = "Pacientes"

        ultimas_personas = (
            db.session.query(Persona)
            .where(Persona.tipo == "M")
            .order_by(desc(Persona.id_persona))
            .limit(10)
        )
    elif tipo == "P":  # Enfermeras
        titulo2 = "Pacientes"

        ultimas_personas = (
            db.session.query(Persona)
            .where(Persona.tipo == "p")
            .order_by(desc(Persona.id_persona))
            .limit(10)
        )
    elif tipo == "E":
        titulo2 = "Empleados"

        ultimas_personas = (
            db.session.query(Persona)
            .where(Persona.tipo == "E")
            .order_by(desc(Persona.id_persona))
            .limit(10)
        )

    return render_template(
        "prin/dashboard.html", datos=ultimas_personas, acc=rutas, t1="", t2=titulo2
    )


@prin_bp.route("/editarPersona/<int:id>")
@login_required
def editarPersona(id):
    per = Persona.get(id)
    return render_template("prin/editarPer.html", dato=per)
