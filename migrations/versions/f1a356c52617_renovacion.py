"""renovacion

Revision ID: f1a356c52617
Revises: 
Create Date: 2024-11-16 12:29:05.612441

"""

from datetime import datetime
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from sqlalchemy.sql import table, column
from werkzeug.security import generate_password_hash

# revision identifiers, used by Alembic.
revision = "f1a356c52617"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "acceso",
        sa.Column("id_acceso", sa.Integer(), nullable=False),
        sa.Column("tipo_usuario", sa.CHAR(length=2), nullable=True),
        sa.Column("nombre_acceso", sa.String(length=20), nullable=True),
        sa.Column("ruta", sa.String(length=120), nullable=True),
        sa.Column("tipo_acceso", sa.CHAR(length=1), nullable=True),
        sa.Column("estado_reg", sa.CHAR(length=1), nullable=True),
        sa.PrimaryKeyConstraint("id_acceso"),
    )
    op.create_table(
        "especialidad",
        sa.Column("id_especialidad", sa.Integer(), nullable=False),
        sa.Column("nombre_especialidad", sa.String(length=40), nullable=True),
        sa.Column("estado_reg", sa.CHAR(length=1), nullable=True),
        sa.PrimaryKeyConstraint("id_especialidad"),
    )
    op.create_table(
        "lista",
        sa.Column("id_lista", sa.Integer(), nullable=False),
        sa.Column("codigo_texto", sa.String(length=3), nullable=True),
        sa.Column("grupo", sa.String(length=20), nullable=True),
        sa.Column("orden", sa.SmallInteger(), nullable=True),
        sa.Column("descripcion", sa.String(length=200), nullable=True),
        sa.Column("estado_reg", sa.CHAR(length=1), nullable=True),
        sa.PrimaryKeyConstraint("id_lista"),
    )
    op.create_table(
        "persona",
        sa.Column("id_persona", sa.Integer(), nullable=False),
        sa.Column("tipo", sa.CHAR(length=1), nullable=True),
        sa.Column("ci", sa.String(length=10), nullable=False),
        sa.Column("nombres", sa.String(length=60), nullable=True),
        sa.Column("paterno", sa.String(length=60), nullable=True),
        sa.Column("materno", sa.String(length=60), nullable=True),
        sa.Column("fecha_nacimiento", sa.Date(), nullable=True),
        sa.Column("sexo", sa.CHAR(length=1), nullable=True),
        sa.Column("fecha_reg", sa.DateTime(), nullable=True),
        sa.Column("usuario_reg", sa.String(length=20), nullable=True),
        sa.Column("ip_reg", sa.String(length=20), nullable=True),
        sa.Column("estado_reg", sa.CHAR(length=1), nullable=True),
        sa.PrimaryKeyConstraint("id_persona"),
        sa.UniqueConstraint("ci"),
    )
    op.create_table(
        "turno",
        sa.Column("id_turno", sa.Integer(), nullable=False),
        sa.Column("dia_semana", sa.CHAR(length=1), nullable=True),
        sa.Column("fecha_inicio", sa.Date(), nullable=True),
        sa.Column("fecha_fin", sa.Date(), nullable=True),
        sa.Column("hora_inicio", sa.Time(), nullable=True),
        sa.Column("hora_fin", sa.Time(), nullable=True),
        sa.Column("estado_turno", sa.String(length=2), nullable=True),
        sa.Column("estado_reg", sa.CHAR(length=1), nullable=True),
        sa.PrimaryKeyConstraint("id_turno"),
    )
    op.create_table(
        "ambiente",
        sa.Column("id_ambiente", sa.Integer(), nullable=False),
        sa.Column("id_especialidad", sa.Integer(), nullable=True),
        sa.Column("nombre_ambiente", sa.String(length=40), nullable=True),
        sa.Column("ubicacion", sa.String(length=60), nullable=True),
        sa.Column("estado_reg", sa.CHAR(length=1), nullable=True),
        sa.ForeignKeyConstraint(
            ["id_especialidad"],
            ["especialidad.id_especialidad"],
        ),
        sa.PrimaryKeyConstraint("id_ambiente"),
    )
    op.create_table(
        "direccion",
        sa.Column("id_direccion", sa.Integer(), nullable=False),
        sa.Column("calle", sa.String(length=60), nullable=True),
        sa.Column("numero_puerta", sa.String(length=5), nullable=True),
        sa.Column("zona", sa.String(length=60), nullable=True),
        sa.Column("ciudad", sa.String(length=40), nullable=True),
        sa.Column("coord", sa.String(length=50), nullable=True),
        sa.Column("id_persona", sa.Integer(), nullable=True),
        sa.Column("estado_reg", sa.CHAR(length=1), nullable=True),
        sa.ForeignKeyConstraint(
            ["id_persona"],
            ["persona.id_persona"],
        ),
        sa.PrimaryKeyConstraint("id_direccion"),
    )
    op.create_table(
        "email",
        sa.Column("id_email", sa.Integer(), nullable=False),
        sa.Column("tipo", sa.CHAR(length=1), nullable=True),
        sa.Column("correo", sa.String(length=200), nullable=True),
        sa.Column("id_persona", sa.Integer(), nullable=True),
        sa.Column("estado_reg", sa.CHAR(length=1), nullable=True),
        sa.ForeignKeyConstraint(
            ["id_persona"],
            ["persona.id_persona"],
        ),
        sa.PrimaryKeyConstraint("id_email"),
    )
    op.create_table(
        "empleado",
        sa.Column("id_empleado", sa.Integer(), nullable=False),
        sa.Column("id_persona", sa.Integer(), nullable=True),
        sa.Column("fecha_ingreso", sa.Date(), nullable=True),
        sa.Column("codigo_marcado", sa.Integer(), nullable=True),
        sa.Column("trato", sa.String(length=10), nullable=True),
        sa.Column("tipo_empleado", sa.CHAR(length=2), nullable=True),
        sa.Column("cargo", sa.String(length=50), nullable=True),
        sa.Column("especialidad", sa.String(length=50), nullable=True),
        sa.ForeignKeyConstraint(
            ["id_persona"],
            ["persona.id_persona"],
        ),
        sa.PrimaryKeyConstraint("id_empleado"),
    )
    op.create_table(
        "familia",
        sa.Column("id_familia", sa.Integer(), nullable=False),
        sa.Column("id_persona1", sa.Integer(), nullable=True),
        sa.Column("id_persona2", sa.Integer(), nullable=True),
        sa.Column("tipo_relacion", sa.String(length=20), nullable=True),
        sa.Column("apellido", sa.String(length=100), nullable=True),
        sa.Column("estado_reg", sa.CHAR(length=1), nullable=True),
        sa.ForeignKeyConstraint(
            ["id_persona1"],
            ["persona.id_persona"],
        ),
        sa.ForeignKeyConstraint(
            ["id_persona2"],
            ["persona.id_persona"],
        ),
        sa.PrimaryKeyConstraint("id_familia"),
    )
    op.create_table(
        "paciente",
        sa.Column("id_paciente", sa.Integer(), nullable=False),
        sa.Column("id_persona", sa.Integer(), nullable=True),
        sa.Column("estado_civil", sa.String(length=1), nullable=True),
        sa.Column("nivel_instruccion", sa.String(length=1), nullable=True),
        sa.Column("tipo_sangre", sa.CHAR(length=3), nullable=True),
        sa.Column("procedencia", postgresql.JSON(astext_type=sa.Text()), nullable=True),
        sa.Column("residencia", postgresql.JSON(astext_type=sa.Text()), nullable=True),
        sa.ForeignKeyConstraint(
            ["id_persona"],
            ["persona.id_persona"],
        ),
        sa.PrimaryKeyConstraint("id_paciente"),
    )
    op.create_table(
        "prestacion",
        sa.Column("id_prestacion", sa.Integer(), nullable=False),
        sa.Column("id_especialidad", sa.Integer(), nullable=True),
        sa.Column("tipo_prestacion", sa.CHAR(length=1), nullable=True),
        sa.Column("descripcion", sa.String(length=200), nullable=True),
        sa.Column("costo", sa.Numeric(precision=8, scale=3), nullable=True),
        sa.Column("estado_reg", sa.CHAR(length=1), nullable=True),
        sa.ForeignKeyConstraint(
            ["id_especialidad"],
            ["especialidad.id_especialidad"],
        ),
        sa.PrimaryKeyConstraint("id_prestacion"),
    )
    op.create_table(
        "telefono",
        sa.Column("id_telefono", sa.Integer(), nullable=False),
        sa.Column("tipo", sa.CHAR(length=1), nullable=True),
        sa.Column("numero", sa.String(length=12), nullable=True),
        sa.Column("id_persona", sa.Integer(), nullable=True),
        sa.Column("estado_reg", sa.CHAR(length=1), nullable=True),
        sa.ForeignKeyConstraint(
            ["id_persona"],
            ["persona.id_persona"],
        ),
        sa.PrimaryKeyConstraint("id_telefono"),
    )
    op.create_table(
        "ficha",
        sa.Column("id_ficha", sa.Integer(), nullable=False),
        sa.Column("id_paciente", sa.Integer(), nullable=True),
        sa.Column("id_turno", sa.Integer(), nullable=True),
        sa.Column("id_prestacion", sa.Integer(), nullable=True),
        sa.Column("id_ambiente", sa.Integer(), nullable=True),
        sa.Column("hora_inicio", sa.Time(), nullable=True),
        sa.Column("hora_fin", sa.Time(), nullable=True),
        sa.Column("estado", sa.CHAR(length=1), nullable=True),
        sa.ForeignKeyConstraint(
            ["id_ambiente"],
            ["ambiente.id_ambiente"],
        ),
        sa.ForeignKeyConstraint(
            ["id_paciente"],
            ["paciente.id_paciente"],
        ),
        sa.ForeignKeyConstraint(
            ["id_prestacion"],
            ["prestacion.id_prestacion"],
        ),
        sa.ForeignKeyConstraint(
            ["id_turno"],
            ["turno.id_turno"],
        ),
        sa.PrimaryKeyConstraint("id_ficha"),
    )
    op.create_table(
        "horario",
        sa.Column("id_horario", sa.Integer(), nullable=False),
        sa.Column("id_empleado", sa.Integer(), nullable=True),
        sa.Column("dia_sem", sa.String(length=2), nullable=True),
        sa.Column("hora_inicio", sa.Time(), nullable=True),
        sa.Column("hora_fin", sa.Time(), nullable=True),
        sa.Column("estado_reg", sa.CHAR(length=1), nullable=True),
        sa.ForeignKeyConstraint(
            ["id_empleado"],
            ["empleado.id_empleado"],
        ),
        sa.PrimaryKeyConstraint("id_horario"),
    )
    op.create_table(
        "usuario",
        sa.Column("id_usuario", sa.Integer(), nullable=False),
        sa.Column("id_empleado", sa.Integer(), nullable=True),
        sa.Column("nombre_usuario", sa.String(length=20), nullable=True),
        sa.Column("clave_usuario", sa.String(length=250), nullable=True),
        sa.Column("email", sa.String(length=250), nullable=True),
        sa.Column("fecha_reg", sa.DateTime(), nullable=True),
        sa.Column("usuario_reg", sa.String(length=20), nullable=True),
        sa.Column("ip_reg", sa.String(length=20), nullable=True),
        sa.Column("estado_reg", sa.CHAR(length=1), nullable=True),
        sa.ForeignKeyConstraint(
            ["id_empleado"],
            ["empleado.id_empleado"],
        ),
        sa.PrimaryKeyConstraint("id_usuario"),
    )
    op.create_table(
        "consulta",
        sa.Column("id_consulta", sa.Integer(), nullable=False),
        sa.Column("id_ficha", sa.Integer(), nullable=True),
        sa.Column("id_empleado", sa.Integer(), nullable=True),
        sa.Column("fecha_atencion", sa.Date(), nullable=True),
        sa.Column("id_paciente", sa.Integer(), nullable=True),
        sa.Column(
            "signos_vitales", postgresql.JSON(astext_type=sa.Text()), nullable=True
        ),
        sa.Column(
            "examen_fisico", postgresql.JSON(astext_type=sa.Text()), nullable=True
        ),
        sa.Column(
            "antecedentes", postgresql.JSON(astext_type=sa.Text()), nullable=True
        ),
        sa.Column(
            "motivo_consulta", postgresql.JSON(astext_type=sa.Text()), nullable=True
        ),
        sa.Column("estado_reg", sa.CHAR(length=1), nullable=True),
        sa.ForeignKeyConstraint(
            ["id_empleado"],
            ["empleado.id_empleado"],
        ),
        sa.ForeignKeyConstraint(
            ["id_ficha"],
            ["ficha.id_ficha"],
        ),
        sa.ForeignKeyConstraint(
            ["id_paciente"],
            ["paciente.id_paciente"],
        ),
        sa.PrimaryKeyConstraint("id_consulta"),
    )
    # ### end Alembic commands ###
    op.execute(
        """
        INSERT INTO lista (codigo_texto, grupo, orden, descripcion, estado_reg) VALUES
        ('V', 'estado_reg', 1, 'Vigente', 'V'),
        ('A', 'estado_reg', 2, 'Anulado', 'V'),
        ('A', 'nivel_instruccion', 1, 'Analfabeto', 'V'),
        ('P', 'nivel_instruccion', 2, 'Primaria', 'V'),
        ('S', 'nivel_instruccion', 3, 'Secundaria', 'V'),
        ('B', 'nivel_instruccion', 4, 'Bachiller', 'V'),
        ('U', 'nivel_instruccion', 5, 'Universitario', 'V'),
        ('F', 'nivel_instruccion', 6, 'Profesional', 'V'),
        ('G', 'nivel_instruccion', 7, 'Pos Grado', 'V'),
        ('D', 'nivel_instruccion', 8, 'Doctorado', 'V'),
        ('S', 'estado_civil', 1, 'Soltero/a', 'V'),
        ('C', 'estado_civil', 2, 'Casado/a', 'V'),
        ('V', 'estado_civil', 3, 'Viudo/a', 'V'),
        ('D', 'estado_civil', 4, 'Divorciado/a', 'V'),
        ('I', 'estado_civil', 5, 'Conviviente', 'V'),
        ('S', 'estado_civil', 6, 'No determinado', 'V'),
        ('V', 'estado', 1, 'Vigente', 'V'),
        ('A', 'estado', 2, 'Anulado', 'V'),
        ('I', 'tipo_prestacion', 3, 'Institucional', 'V'),
        ('S', 'tipo_prestacion', 1, 'Seguro SUS', 'V'),
        ('O', 'tipo_prestacion', 2, 'SOAP', 'V'),
        ('L', 'dia_semana', 1, 'Lunes', 'V'),
        ('M', 'dia_semana', 2, 'Martes', 'V'),
        ('I', 'dia_semana', 3, 'Miércoles', 'V'),
        ('J', 'dia_semana', 4, 'Jueves', 'V'),
        ('V', 'dia_semana', 5, 'Viernes', 'V'),
        ('S', 'dia_semana', 6, 'Sábado', 'V'),
        ('D', 'dia_semana', 7, 'Domingo', 'V'),
        ('M', 'tipo_empleado', 1, 'Médico', 'V'),
        ('E', 'tipo_empleado', 2, 'Enfermera', 'V'),
        ('T', 'tipo_empleado', 3, 'Técnico Area Médica', 'V'),
        ('AP', 'tipo_empleado', 4, 'Profesional Admministrativo', 'V'),
        ('AT', 'tipo_empleado', 5, 'Técnico Admministrativo', 'V'),
        ('AS', 'tipo_empleado', 6, 'Admministrador de Sistemas', 'V'),
        ('AO', 'tipo_empleado', 7, 'Operador Admministrativo', 'V'),
        ('E', 'tipo_persona', 1, 'Empleado', 'V'),
        ('P', 'tipo_persona', 3, 'Paciente', 'V');
        """
    )
    op.execute(
        """
            INSERT INTO especialidad (nombre_especialidad) VALUES
                ('Medicina General'),
                ('Ginecología'),
                ('Pediatría'),
                ('Cirugía'),
                ('Traumatología'),
                ('Ecografía'),
                ('Fisioterapia');
        """
    )
    op.execute(
        """
        INSERT INTO prestacion (id_especialidad, tipo_prestacion, descripcion, costo) VALUES
            (1, 'I', 'Consulta Externa', 20),
            (2, 'I', 'Consulta de Esp. Ginecología', 25),
            (3, 'I', 'Consulta de Esp. Pediatría', 25),
            (4, 'I', 'Consulta de Esp. Cirugía', 25),
            (5, 'I', 'Consulta de Esp. Traumatología', 25),
            (6, 'I', 'Ecografía obstétrica', 60),
            (6, 'I', 'Ecografía abdominal', 120),
            (7, 'I', 'Sesión de Fisioterapia', 20);
        """
    )

    op.execute(
        """
            INSERT INTO persona (id_persona, tipo, ci, nombres, paterno, materno, fecha_nacimiento, sexo, fecha_reg, usuario_reg, ip_reg, estado_reg) VALUES
            (1, 'E', '7520145', 'Luis Eduardo', 'Perez', 'Vargas', '1990-05-15', 'M', '2024-10-30 09:34:11', 'admin', '192.168.0.1', 'V'),
            (2, 'E', '8053145', 'Maria Alejandra', 'Gomez', 'Rojas', '1985-11-21', 'F', '2024-10-30 09:35:11', 'admin', '192.168.0.2', 'A'),
            (3, 'E', '8521097', 'Carlos Alberto', 'Sanchez', 'Quiroga', '1992-02-20', 'M', '2024-10-30 09:36:11', 'admin', '192.168.0.3', 'V'),
            (4, 'E', '3379293', 'Elvis Roger', 'Anavi', 'Jimenez', '1968-11-13', 'M', '2024-10-30 19:36:11', 'admin', '192.168.0.3', 'V'),
            (5, 'M', '8541244', 'Nemesio Alberto', 'Mendoza', 'Antezana', '1991-01-20', 'M', '2024-10-30 09:36:11', 'admin', '192.168.0.3', 'V'),
            (6, 'M', '8454467', 'Miguel Carlos', 'Sotomayor', 'Carrasco', '1970-03-20', 'M', '2024-10-30 09:36:11', 'admin', '192.168.0.3', 'V'),
            (7, 'M', '8755454', 'Malori', 'Boutier', 'Fernandez', '1970-02-27', 'F', '2024-10-30 09:36:11', 'admin', '192.168.0.3', 'V'),
            (8, 'P', '8653135', 'Carla Monica', 'Condarco', 'Espinoza', '1980-02-27', 'F', '2024-10-30 09:36:11', 'admin', '192.168.0.3', 'V'),
            (9, 'P', '7874212', 'Fernanda Amada', 'Ticona', 'Quispe', '1970-02-27', 'F', '2024-10-30 09:36:11', 'admin', '192.168.0.3', 'V'),
            (10, 'P', '98413241', 'Ernesto Miguel', 'Negrete', 'Guardia', '1967-08-15', 'M', '2024-10-30 09:36:11', 'admin', '192.168.0.3', 'V');

        """
    )

    op.execute(
        """
            INSERT INTO empleado (id_empleado, id_persona, fecha_ingreso, codigo_marcado, trato, tipo_empleado, cargo, especialidad) VALUES
            (1, 1, '2015-08-20', 1001, 'Sr.', 'AP', 'Administrador', 'Administrador de Empresas'),
            (2, 2, '2017-03-14', 1002, 'Sra.', 'AT', 'Admisionista', 'Atención al Cliente'),
            (3, 3, '2018-07-09', 1003, 'Sr.', 'AO', 'Encargado de Limpieza', 'Manual'),
            (4, 4, '2024-01-01', 1004, 'Sr.', 'AS', 'Administrador de Sistemas', 'Ing. de Sistemas'),
            (5, 5, '2024-01-01', 1005, 'Dr.', 'M', 'Cardiólogo', 'Médico Cardiólogo'),
            (6, 6, '2024-01-01', 1006, 'Dr.', 'E', 'Enfermera', 'Enfermera instrumentista'),
            (7, 7, '2024-01-01', 1007, 'Dr.','M', 'Médico General', 'Médico General');
        """
    )

    op.execute(
        """
            INSERT INTO paciente (id_paciente, id_persona, estado_civil, nivel_instruccion, tipo_sangre, procedencia, residencia) VALUES
            (1, 8, 'S', 'U', 'O+', '{"ciudad": "La Paz"}', '{"ciudad": "Cochabamba"}'),
            (2, 9, 'C', 'B', 'A-', '{"ciudad": "Santa Cruz"}', '{"ciudad": "Santa Cruz"}'),
            (3, 10, 'D', 'G', 'B+', '{"ciudad": "Oruro"}', '{"ciudad": "Potosí"}');

            INSERT INTO horario (id_horario, id_empleado, dia_sem, hora_inicio, hora_fin, estado_reg) VALUES
            (1, 2, 'L', '08:00:00', '16:00:00', 'V'),
            (2, 3, 'M', '09:00:00', '17:00:00', 'A');

            INSERT INTO ambiente (id_ambiente, id_especialidad, nombre_ambiente, ubicacion, estado_reg) VALUES
            (1, 1, 'Consultorio 101', 'Planta Baja', 'V'),
            (2, 2, 'Consultorio 102', 'Primer Piso', 'A'),
            (3, 3, 'Consultorio 103', 'Segundo Piso', 'V');

            INSERT INTO turno (id_turno, dia_semana, fecha_inicio, fecha_fin, hora_inicio, hora_fin, estado_turno, estado_reg) VALUES
            (1, 'L', '2024-10-01', '2024-10-15', '08:00:00', '12:00:00', 'V', 'V'),
            (2, 'M', '2024-10-02', '2024-10-16', '14:00:00', '18:00:00', 'V', 'A');

            INSERT INTO ficha (id_ficha, id_paciente, id_turno, id_prestacion, id_ambiente, hora_inicio, hora_fin, estado) VALUES
            (1, 1, 1, 1, 1, '08:00:00', '08:30:00', 'V'),
            (2, 2, 2, 2, 2, '14:00:00', '14:30:00', 'A');

            INSERT INTO consulta (id_consulta, id_ficha, id_empleado, fecha_atencion, id_paciente, signos_vitales, examen_fisico, antecedentes, motivo_consulta, estado_reg) VALUES
            (1, 1, 5, '2024-10-14', 1, '{"presion": "120/80"}', '{"piel": "Normal"}', '{"alergias": "ninguna"}', '{"sintomas": "dolor pecho"}', 'V'),
            (2, 2, 7, '2024-10-15', 2, '{"presion": "110/70"}', '{"piel": "Pálida"}', '{"asma": "controlada"}', '{"sintomas": "fiebre alta"}', 'A');

            INSERT INTO telefono (id_telefono, tipo, numero, id_persona, estado_reg) VALUES
            (1, 'M', '699876543', 1, 'V'),
            (2, 'C', '442233567', 2, 'A');

            INSERT INTO email (id_email, tipo, correo, id_persona, estado_reg) VALUES
            (1, 'P', 'luis.perez@gmail.com', 1, 'V'),
            (2, 'T', 'maria.rojas@gmail.com', 2, 'A');

            INSERT INTO direccion (id_direccion, calle, numero_puerta, zona, ciudad, coord, id_persona, estado_reg) VALUES
            (1, 'Av. La Paz', '123', 'Centro', 'La Paz', '-16.5,-68.1', 1, 'V'),
            (2, 'Av. Santa Cruz', '456', 'Norte', 'Santa Cruz', '-17.8,-63.1', 2, 'A');

        """
    )

    op.execute(
        """
        INSERT INTO acceso 
        (tipo_usuario, nombre_acceso, ruta, tipo_acceso, estado_reg) VALUES
        ('M', 'Pacientes', 'pacientes', 'G', 'V'),
        ('M', 'Fichas', 'fichas', 'V', 'V'),
        ('M', 'Turnos', 'turnos', 'V', 'V'),
        
        ('AT','Pacienes', 'pacientes', 'G', 'V'),
        ('AT','Fichas', 'fichas', 'G', 'V'),
        ('AT','Turnos', 'turnos', 'G', 'V'),
        
        ('AS','Pacientes', 'pacientes', 'G', 'V'),
        ('AS','Empleados', 'empleados', 'G', 'V'),
        ('AS','Fichas', 'fichas', 'G', 'V'),
        ('AS','Turnos', 'turnos', 'G', 'V'),
        ('AS','Especialidades', 'especialidades', 'G', 'V'),
        ('AS','Usuarios', 'usuarios', 'G', 'V'),
        ('AS','Prestaciones', 'prestaciones', 'G', 'V'),
        
        ('E', 'Pacientes', 'pacientes', 'V', 'V'),
        ('E', 'Fichas', 'fichas', 'V', 'V'),
        ('E', 'Turnos', 'tukrnos', 'V', 'V');
        """
    )

    tbl_usuario = table(
        "usuario",
        column("id_usuario", sa.Integer),
        column("id_empleado", sa.Integer),
        column("nombre_usuario", sa.String(length=20)),
        column("clave_usuario", sa.String(length=250)),
        column("email", sa.String(length=250)),
        column("fecha_reg", sa.DateTime()),
        column("usuario_reg", sa.String(length=20)),
        column("ip_reg", sa.String(length=20)),
        column("estado_reg", sa.CHAR(length=1)),
    )

    op.bulk_insert(
        tbl_usuario,
        [
            {
                "id_usuario": 1,
                "id_empleado": 4,
                "nombre_usuario": "eanavi",
                "clave_usuario": generate_password_hash("vicho.1368"),
                "email": "eanavi@gmail.com",
                "fecha_reg": datetime.now(),
                "usuario_reg": "eanavi",
                "ip_reg": "192.168.0.1",
                "estado_reg": "V",
            },
            {
                "id_usuario": 2,
                "id_empleado": 2,
                "nombre_usuario": "luisadmin",
                "clave_usuario": generate_password_hash("luisadmin"),
                "email": "luis@admin.com",
                "fecha_reg": datetime.now(),
                "usuario_reg": "eanavi",
                "ip_reg": "192.168.7.1",
                "estado_reg": "V",
            },
            {
                "id_usuario": 3,
                "id_empleado": 1,
                "nombre_usuario": "mariaemp",
                "clave_usuario": generate_password_hash("mariaemp"),
                "email": "mariaemp@gmail.com",
                "fecha_reg": datetime.now(),
                "usuario_reg": "eanavi",
                "ip_reg": "192.168.9.1",
                "estado_reg": "V",
            },
        ],
    )


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("consulta")
    op.drop_table("usuario")
    op.drop_table("horario")
    op.drop_table("ficha")
    op.drop_table("telefono")
    op.drop_table("prestacion")
    op.drop_table("paciente")
    op.drop_table("familia")
    op.drop_table("empleado")
    op.drop_table("email")
    op.drop_table("direccion")
    op.drop_table("ambiente")
    op.drop_table("turno")
    op.drop_table("persona")
    op.drop_table("lista")
    op.drop_table("especialidad")
    op.drop_table("acceso")
    # ### end Alembic commands ###
