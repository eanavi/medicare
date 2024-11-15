from flask import render_template
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

    if tipo == "M":  # Medicos
        titulo = "Medico"
        titulo2 = "Pacientes"
        rutas = Acceso.query.where(Acceso.tipo_usuario == "M")

        ultimas_personas = (
            db.session.query(Persona)
            .where(Persona.tipo == "p", Persona.estado_reg == "V")
            .order_by(desc(Persona.id_persona))
            .limit(10)
            .all()
        )
    elif tipo == "E":  # Enfermeras
        titulo = "Enfermera"
        titulo2 = "Pacientes"
        rutas = Acceso.query.where(Acceso.tipo_usuario == "M")

        ultimas_personas = (
            db.session.query(Persona)
            .where(Persona.tipo == "p", Persona.estado_reg == "V")
            .order_by(desc(Persona.id_persona))
            .limit(10)
            .all()
        )
    elif tipo == "AP":
        titulo = "Profesional Administrativo"
        titulo2 = "Empleados"
        rutas = Acceso.query.where(Acceso.tipo_usuario == "E")

        ultimas_personas = (
            db.session.query(Persona)
            .where(
                Persona.tipo == "E",
                Persona.estado_reg == "V",
            )
            .order_by(desc(Persona.id_persona))
            .limit(10)
            .all()
        )
    elif tipo == "AT":
        titulo = "Tecnico Administrativo"
        titulo2 = "Personas"
        rutas = Acceso.query.where(Acceso.tipo_usuario == "T")

        ultimas_personas = (
            db.session.query(Persona)
            .where(Persona.tipo == "P", Persona.estado_reg == "V")
            .order_by(desc(Persona.id_persona))
            .limit(10)
            .all()
        )
    elif tipo == "AS":
        titulo = "Administrador de Sistemas"
        titulo2 = "Empleados"
        rutas = Acceso.query.filter(Acceso.tipo_usuario == "T")

        ultimas_personas = (
            db.session.query(Persona)
            .where(Persona.tipo == "E", Persona.estado_reg == "V")
            .order_by(desc(Persona.id_persona))
            .limit(10)
            .all()
        )

    return render_template(
        "prin/dashboard.html", datos=ultimas_personas, acc=rutas, t1=titulo, t2=titulo2
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
