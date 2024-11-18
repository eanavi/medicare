from flask import jsonify
from sqlalchemy import text
from flask_login import login_required

from . import api_bp
from ..modelo import db


@api_bp.route("/turnos")
@login_required
def get_turnos():
    consulta = "select t.id_turno, t.fecha_inicio, t.fecha_fin, t.dia_semana, \
                    s.nombre_especialidad, p.nombres, p.paterno, p.materno \
                from turno t inner join empleado as  e on t.id_empleado  = e.id_empleado \
                             inner join persona as p on e.id_persona  = p.id_persona \
                             inner join especialidad s on e.id_especialidad  = s.id_especialidad \
                 where tipo_empleado = 'M' order by s.nombre_especialidad"
    # EmpleadoAlias = aliased(Empleado)
    # PersonaAlias = aliased(Persona)
    # EspecialidadAlias = aliased(Especialidad)
    # query = (
    #     db.session.query(
    #         Turno.id_turno,
    #         Turno.fecha_inicio,
    #         Turno.fecha_fin,
    #         Turno.dia_semana,
    #         EspecialidadAlias.nombre_especialidad,
    #         PersonaAlias.nombres,
    #         PersonaAlias.paterno,
    #         PersonaAlias.materno,
    #     )
    #     .join(EmpleadoAlias, Turno.id_empleado == EmpleadoAlias.id_empleado)
    #     .join(PersonaAlias, EmpleadoAlias.id_persona == PersonaAlias.id_persona)
    #     .join(
    #         EspecialidadAlias,
    #         EmpleadoAlias.id_especialidad == EspecialidadAlias.id_especialidad,
    #     )
    #     .filter(EmpleadoAlias.tipo_empleado == "M")  # Filtro para tipo_empleado
    #     .order_by(
    #         EspecialidadAlias.nombre_especialidad.asc()
    #     )  # Ordenar por especialidad
    # )
    resultado = db.session.execute(text(consulta))
    resultado_json = [
        {
            "id_turno": linea.id_turno,
            "fecha_inicio": linea.fecha_inicio,
            "fecha_fin": linea.fecha_fin,
            "dia_semana": linea.dia_semana,
            "nombre_especialidad": linea.nombre_especialidad,
            "nombres": linea.nombres,
            "paterno": linea.paterno,
            "materno": linea.materno,
        }
        for linea in resultado
    ]
    return jsonify(resultado_json)


@api_bp.route("/turno/busca/<string:criterio>/<string:tipo>")
@login_required
def get_busca_turno(criterio, tipo):
    consulta = "select t.id_turno, t.fecha_inicio, t.fecha_fin, t.dia_semana, \
                    s.nombre_especialidad, p.nombres, p.paterno, p.materno \
                from turno t inner join empleado as  e on t.id_empleado  = e.id_empleado \
                             inner join persona as p on e.id_persona  = p.id_persona \
                             inner join especialidad s on e.id_especialidad  = s.id_especialidad \
                 where tipo_empleado = 'M' order by s.nombre_especialidad"
    resultado = db.session.execute(text(consulta))
    resultado_json = [
        {
            "id_turno": linea.id_turno,
            "fecha_inicio": linea.fecha_inicio,
            "fecha_fin": linea.fecha_fin,
            "dia_semana": linea.dia_semana,
            "nombre_especialidad": linea.nombre_especialidad,
            "nombres": linea.nombres,
            "paterno": linea.paterno,
            "materno": linea.materno,
        }
        for linea in resultado
    ]
    return jsonify(resultado_json)
