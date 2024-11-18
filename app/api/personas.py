from flask import jsonify
from sqlalchemy import func
from flask_login import login_required

from . import api_bp
from ..modelo import Persona, db
from ..auxiliar import otr


@api_bp.route("/personas")
@login_required
def get_personas():
    pers = Persona.query.all()
    return jsonify({"personas": [per.to_json() for per in pers]})


@api_bp.route("/persona/<int:id>")
def get_persona_id(id):
    per = Persona.query.get_or_404(id)
    return jsonify(per.to_json())


"""           tambien puede funcionar con
pers = db.session.query(Persona).filter(
            Persona.tipo == con,
            Persona.fecha_nacimiento == otr.tipo_fecha(criterio),
            Persona.estado_reg == 'V'
        )
"""


@api_bp.route("/persona/busca/<string:criterio>/<string:tipo>")
@login_required
def get_busca_persona_tipo(criterio, tipo):
    con = tipo if tipo in ["E", "P"] else "P"
    pers = []
    tipo_dato = otr.determinar_tipo(criterio)
    if tipo_dato == "Numero":
        pers = Persona.query.filter(
            Persona.tipo == con,
            Persona.ci.like(f"%{criterio}%"),
            Persona.estado_reg == "V",
        ).all()

    if tipo_dato == "Fecha":
        pers = Persona.query.filter(
            Persona.tipo == con,
            Persona.fecha_nacimiento == otr.tipo_fecha(criterio),
            Persona.estado_reg == "V",
        )

    if tipo_dato == "Texto":
        nomb = criterio.split()
        if len(nomb) == 1:
            pers = Persona.query.filter(
                Persona.tipo == con,
                func.upper(Persona.paterno).like(func.upper(f"%{nomb[0]}%")),
                Persona.estado_reg == "V",
            )
            print(str(pers.statement))

        if len(nomb) == 2:
            pers = Persona.query.filter(
                Persona.tipo == con,
                func.upper(Persona.nombres).like(func.upper(f"%{nomb[0]}%")),
                func.upper(Persona.paterno).like(func.upper(f"%{nomb[1]}%")),
                Persona.estado_reg == "V",
            )
        if len(nomb) == 3:
            pers = Persona.query.filter(
                Persona.tipo == con,
                func.upper(Persona.nombres).like(func.upper(f"%{nomb[0]}%")),
                func.upper(Persona.paterno).like(func.upper(f"%{nomb[1]}%")),
                func.upper(Persona.materno).like(func.upper(f"%{nomb[2]}%")),
                Persona.estado_reg == "V",
            )

    return jsonify({"persona": [per.to_json() for per in pers]})
