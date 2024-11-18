from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import (
    CheckConstraint,
    UniqueConstraint,
    ForeignKey,
    ForeignKeyConstraint,
    CHAR,
)
from sqlalchemy.dialects.postgresql import JSON
from ext import db


# Clase base de Persona
class Persona(db.Model):
    __tablename__ = "persona"

    id_persona = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(CHAR(1), CheckConstraint("tipo in ('E', 'P')"))
    ci = db.Column(db.String(10), unique=True, nullable=False)
    nombres = db.Column(db.String(60))
    paterno = db.Column(db.String(60))
    materno = db.Column(db.String(60))
    fecha_nacimiento = db.Column(db.Date)
    sexo = db.Column(CHAR(1), CheckConstraint("sexo IN ('M', 'F', 'N')"))
    fecha_reg = db.Column(db.DateTime, default=db.func.current_timestamp())
    usuario_reg = db.Column(db.String(20))
    ip_reg = db.Column(db.String(20))
    estado_reg = db.Column(CHAR(1), CheckConstraint("estado_reg IN ('V', 'A')"))

    def __init__(
        self,
        tipo,
        ci,
        nombres,
        paterno,
        materno,
        sexo,
        fecha_reg,
        usuario_reg,
        ip_reg,
        estado_reg,
    ):
        self.tipo = tipo
        self.ci = ci
        self.nombres = nombres
        self.paterno = paterno
        self.materno = materno
        self.sexo = sexo
        self.fecha_reg = fecha_reg
        self.usuario_reg = usuario_reg
        self.ip_reg = ip_reg
        self.estado_reg = estado_reg

    def to_json(cls):
        per_json = {
            "id_persona": cls.id_persona,
            "tipo": cls.tipo,
            "ci": cls.ci,
            "nombres": cls.nombres,
            "paterno": cls.paterno,
            "materno": cls.materno,
            "fecha_nacimiento": cls.fecha_nacimiento,
            "sexo": cls.sexo,
        }
        return per_json


# Empleado hereda de Persona
class Empleado(Persona):
    __tablename__ = "empleado"

    id_empleado = db.Column(db.Integer, primary_key=True)
    id_persona = db.Column(db.Integer, db.ForeignKey("persona.id_persona"))
    fecha_ingreso = db.Column(db.Date)
    codigo_marcado = db.Column(db.Integer)
    trato = db.Column(db.String(10))
    tipo_empleado = db.Column(
        CHAR(2),
        CheckConstraint("tipo_empleado IN ('M', 'E', 'T', 'AP', 'AT', 'AS', 'AO')"),
    )
    cargo = db.Column(db.String(50))
    id_especialidad = db.Column(
        db.Integer, db.ForeignKey("especialidad.id_especialidad")
    )

    def __init__(
        self,
        tipo,
        ci,
        nombres,
        paterno,
        materno,
        sexo,
        fecha_reg,
        usuario_reg,
        ip_reg,
        estado_reg,
        fecha_ingreso,
        codigo_marcado,
        trato,
        tipo_empleado,
        cargo,
        especialidad,
    ):
        super().__init__(
            tipo,
            ci,
            nombres,
            paterno,
            materno,
            sexo,
            fecha_reg,
            usuario_reg,
            ip_reg,
            estado_reg,
        )
        self.fecha_ingreso = fecha_ingreso
        self.codigo_marcado = codigo_marcado
        self.trato = trato
        self.tipo_empleado = tipo_empleado
        self.cargo = cargo
        self.especialidad = especialidad

    def to_json(self):
        emp_js = super().to_json()
        emp_js.update(
            {
                "id_empleado": self.id_empleado,
                "fecha_ingreso": self.fecha_ingreso,
                "codigo_marcado": self.codigo_marcado,
                "trato": self.trato,
                "tipo_empleado": self.tipo_empleado,
                "cargo": self.cargo,
                "self": self.especialidad,
            }
        )
        return emp_js


# Paciente hereda de Persona
class Paciente(Persona):
    __tablename__ = "paciente"

    id_paciente = db.Column(db.Integer, primary_key=True)
    id_persona = db.Column(db.Integer, db.ForeignKey("persona.id_persona"))
    estado_civil = db.Column(
        db.String(1), CheckConstraint("estado_civil IN ('S', 'C', 'V', 'D', 'N')")
    )
    nivel_instruccion = db.Column(
        db.String(1),
        CheckConstraint(
            "nivel_instruccion IN ('A', 'P', 'S', 'B', 'U', 'F', 'G', 'D')"
        ),
    )
    tipo_sangre = db.Column(
        CHAR(3),
        CheckConstraint(
            "tipo_sangre IN ('AB+', 'AB-','A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'N')"
        ),
    )
    procedencia = db.Column(JSON)
    residencia = db.Column(JSON)

    def __init__(
        self,
        tipo,
        ci,
        nombres,
        paterno,
        materno,
        sexo,
        fecha_reg,
        usuario_reg,
        ip_reg,
        estado_reg,
        estado_civil,
        nivel_instruccion,
        tipo_sangre,
        procedecia,
        residencia,
    ):
        super().__init__(
            tipo,
            ci,
            nombres,
            paterno,
            materno,
            sexo,
            fecha_reg,
            usuario_reg,
            ip_reg,
            estado_reg,
        )
        self.estado_civil = estado_civil
        self.nivel_instruccion = nivel_instruccion
        self.tipo_sangre = tipo_sangre
        self.procedencia = procedecia
        self.residencia = residencia

    def to_json(cls):
        pac_js = super().to_json()
        pac_js.update(
            {
                "id_paciente": cls.id_paciente,
                "estado_civil": cls.estado_civil,
                "nivel_instruccion": cls.nivel_instruccion,
                "tipo_sangre": cls.tipo_sangre,
                "procedencia": cls.procedencia,
                "residencia": cls.residencia,
            }
        )
        return pac_js


class Familia(db.Model):
    __tablename__ = "familia"

    id_familia = db.Column(db.Integer, primary_key=True)
    id_persona1 = db.Column(db.Integer, ForeignKey("persona.id_persona"))
    id_persona2 = db.Column(db.Integer, ForeignKey("persona.id_persona"))
    tipo_relacion = db.Column(db.String(20))
    apellido = db.Column(db.String(100))
    estado_reg = db.Column(CHAR(1), CheckConstraint("estado_reg IN ('V', 'A')"))

    def to_json(self):
        return {
            "id_familia": self.id_familia,
            "id_persona1": self.id_persona1,
            "id_persona2": self.id_persona2,
            "tipo_relacion": self.tipo_relacion,
            "apellido": self.apellido,
            "estado_reg": self.estado_reg,
        }


class Especialidad(db.Model):
    __tablename__ = "especialidad"

    id_especialidad = db.Column(db.Integer, primary_key=True)
    nombre_especialidad = db.Column(db.String(40))
    estado_reg = db.Column(CHAR(1), CheckConstraint("estado_reg IN ('V', 'A')"))

    def to_json(self):
        especialidad = {
            "id_especialidad": self.id_especialidad,
            "nombre_especialidad": self.nombre_especialidad,
        }

        return especialidad


class Ambiente(db.Model):
    __tablename__ = "ambiente"

    id_ambiente = db.Column(db.Integer, primary_key=True)
    id_especialidad = db.Column(db.Integer, ForeignKey("especialidad.id_especialidad"))
    nombre_ambiente = db.Column(db.String(40))
    ubicacion = db.Column(db.String(60))
    estado_reg = db.Column(CHAR(1), CheckConstraint("estado_reg IN ('V', 'A')"))

    def to_json(self):
        return {
            "id_ambiente": self.id_ambiente,
            "id_especialidad": self.id_especialidad,
            "nombre_ambiente": self.nombre_ambiente,
            "ubicacion": self.ubicacion,
            "estado_reg": self.estado_reg,
        }


class Prestacion(db.Model):
    __tablename__ = "prestacion"

    id_prestacion = db.Column(db.Integer, primary_key=True)
    id_especialidad = db.Column(db.Integer, ForeignKey("especialidad.id_especialidad"))
    tipo_prestacion = db.Column(
        CHAR(1), CheckConstraint("tipo_prestacion IN ('I', 'S', 'O')")
    )
    descripcion = db.Column(db.String(200))
    costo = db.Column(db.Numeric(8, 3))
    estado_reg = db.Column(CHAR(1), CheckConstraint("estado_reg IN ('V', 'A')"))

    def to_json(self):
        return {
            "id_prestacion": self.id_prestacion,
            "id_especialidad": self.id_especialidad,
            "tipo_prestacion": self.tipo_prestacion,
            "descripcion": self.descripcion,
            "costo": self.costo,
            "estado_reg": self.estado_reg,
        }


class Turno(db.Model):
    __tablename__ = "turno"

    id_turno = db.Column(db.Integer, primary_key=True)
    id_empleado = db.Column(db.Integer, ForeignKey("empleado.id_empleado"))
    dia_semana = db.Column(
        CHAR(1),
        CheckConstraint("dia_semana IN ('L', 'M', 'I', 'J', 'V', 'S', 'D')"),
    )
    fecha_inicio = db.Column(db.Date)
    fecha_fin = db.Column(db.Date)
    hora_inicio = db.Column(db.Time)
    hora_fin = db.Column(db.Time)
    estado_turno = db.Column(db.String(2))
    estado_reg = db.Column(CHAR(1), CheckConstraint("estado_reg IN ('V', 'A')"))

    def to_json(self):
        return {
            "id_turno": self.id_turno,
            "dia_semana": self.dia_semana,
            "fecha_inicio": self.fecha_inicio,
            "fecha_fin": self.fecha_fin,
            "hora_inicio": self.hora_inicio,
            "hora_fin": self.hora_fin,
            "estado_turno": self.estado_turno,
            "estado_reg": self.estado_reg,
        }


class Ficha(db.Model):
    __tablename__ = "ficha"

    id_ficha = db.Column(db.Integer, primary_key=True)
    id_paciente = db.Column(db.Integer, ForeignKey("paciente.id_paciente"))
    id_turno = db.Column(db.Integer, ForeignKey("turno.id_turno"))
    id_prestacion = db.Column(db.Integer, ForeignKey("prestacion.id_prestacion"))
    id_ambiente = db.Column(db.Integer, ForeignKey("ambiente.id_ambiente"))
    hora_inicio = db.Column(db.Time)
    hora_fin = db.Column(db.Time)
    estado = db.Column(CHAR(1), CheckConstraint("estado IN ('V', 'A')"))

    def to_json(self):
        return {
            "id_ficha": self.id_ficha,
            "id_paciente": self.id_paciente,
            "id_turno": self.id_turno,
            "id_prestacion": self.id_prestacion,
            "id_ambiente": self.id_ambiente,
            "hora_inicio": self.hora_inicio,
            "hora_fin": self.hora_fin,
            "estado": self.estado,
        }


class Consulta(db.Model):
    __tablename__ = "consulta"

    id_consulta = db.Column(db.Integer, primary_key=True)
    id_ficha = db.Column(db.Integer, ForeignKey("ficha.id_ficha"))
    id_empleado = db.Column(db.Integer, ForeignKey("empleado.id_empleado"))
    fecha_atencion = db.Column(db.Date)
    id_paciente = db.Column(db.Integer, ForeignKey("paciente.id_paciente"))
    signos_vitales = db.Column(JSON)
    examen_fisico = db.Column(JSON)
    antecedentes = db.Column(JSON)
    motivo_consulta = db.Column(JSON)
    estado_reg = db.Column(CHAR(1), CheckConstraint("estado_reg IN ('V', 'A')"))

    def to_json(self):
        return {
            "id_consulta": self.id_consulta,
            "id_ficha": self.id_ficha,
            "id_empleado": self.id_empleado,
            "fecha_atencion": self.fecha_atencion,
            "id_paciente": self.id_paciente,
            "signos_vitales": self.signos_vitales,
            "examen_fisico": self.examen_fisico,
            "antecedentes": self.antecedentes,
            "motivo_consulta": self.motivo_consulta,
            "estado_reg": self.estado_reg,
        }


class Telefono(db.Model):
    __tablename__ = "telefono"

    id_telefono = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(CHAR(1))
    numero = db.Column(db.String(12))
    id_persona = db.Column(db.Integer, ForeignKey("persona.id_persona"))
    estado_reg = db.Column(CHAR(1), CheckConstraint("estado_reg IN ('V', 'A')"))

    def to_json(self):
        return {
            "id_telefono": self.id_telefono,
            "tipo": self.tipo,
            "numero": self.numero,
            "id_persona": self.id_persona,
            "estado_reg": self.estado_reg,
        }


class Email(db.Model):
    __tablename__ = "email"

    id_email = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(CHAR(1))
    correo = db.Column(db.String(200))
    id_persona = db.Column(db.Integer, ForeignKey("persona.id_persona"))
    estado_reg = db.Column(CHAR(1), CheckConstraint("estado_reg IN ('V', 'A')"))

    def to_json(self):
        return {
            "id_email": self.id_email,
            "tipo": self.tipo,
            "correo": self.correo,
            "id_persona": self.id_persona,
            "estado_reg": self.estado_reg,
        }


class Direccion(db.Model):
    __tablename__ = "direccion"

    id_direccion = db.Column(db.Integer, primary_key=True)
    calle = db.Column(db.String(60))
    numero_puerta = db.Column(db.String(5))
    zona = db.Column(db.String(60))
    ciudad = db.Column(db.String(40))
    coord = db.Column(db.String(50))
    id_persona = db.Column(db.Integer, ForeignKey("persona.id_persona"))
    estado_reg = db.Column(CHAR(1), CheckConstraint("estado_reg IN ('V', 'A')"))

    def to_json(self):
        return {
            "id_direccion": self.id_direccion,
            "calle": self.calle,
            "numero_puerta": self.numero_puerta,
            "zona": self.numero_puerta,
            "ciudad": self.ciudad,
            "coord": self.coord,
            "id_persona": self.id_persona,
            "estado_reg": self.estado_reg,
        }


class Usuario(UserMixin, db.Model):
    __tablename__ = "usuario"

    id_usuario = db.Column(db.Integer, primary_key=True)
    id_empleado = db.Column(db.Integer, ForeignKey("empleado.id_empleado"))
    nombre_usuario = db.Column(db.String(20))
    clave_usuario = db.Column(db.String(250))
    email = db.Column(db.String(250))
    fecha_reg = db.Column(db.DateTime, default=db.func.current_timestamp())
    usuario_reg = db.Column(db.String(20))
    ip_reg = db.Column(db.String(20))
    estado_reg = db.Column(CHAR(1), CheckConstraint("estado_reg IN ('V', 'A')"))

    def to_json(self):
        return {
            "id_usuario": self.id_usuario,
            "id_empleado": self.id_empleado,
            "nombre_usuario": self.nombre_usuario,
            "clave_usuario": self.clave_usuario,
            "email": self.email,
            "fecha_reg": self.fecha_reg,
            "usuario_reg": self.usuario_reg,
            "ip_reg": self.ip_reg,
            "estado_reg": self.estado_reg,
        }

    def set_password(self, password):
        self.clave_usuario = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.clave_usuario, password)

    def get_id(self):
        return str(self.id_usuario)


class Lista(db.Model):
    __tablename__ = "lista"

    id_lista = db.Column(db.Integer, primary_key=True)
    codigo_texto = db.Column(db.String(3))
    grupo = db.Column(db.String(20))
    orden = db.Column(db.SmallInteger)
    descripcion = db.Column(db.String(200))
    estado_reg = db.Column(CHAR(1), CheckConstraint("estado_reg IN ('V', 'A')"))

    def to_json(self):
        return {
            "id_lista": self.id_lista,
            "codigo_texto": self.codigo_texto,
            "grupo": self.grupo,
            "orden": self.orden,
            "descripcion": self.descripcion,
            "estado_reg": self.estado_reg,
        }


class Acceso(db.Model):
    __tablename__ = "acceso"

    id_acceso = db.Column(db.Integer, primary_key=True)
    tipo_usuario = db.Column(
        CHAR(2), CheckConstraint("tipo_usuario IN ('M', 'E', 'T', 'AP', 'AT', 'AS')")
    )
    nombre_acceso = db.Column(db.String(20))
    ruta = db.Column(db.String(120))
    tipo_acceso = db.Column(CHAR(1), CheckConstraint("tipo_acceso IN ('G', 'V')"))
    estado_reg = db.Column(CHAR(1), CheckConstraint("estado_reg IN ('V', 'A')"))
