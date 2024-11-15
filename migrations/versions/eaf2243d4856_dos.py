"""dos

Revision ID: eaf2243d4856
Revises: 7d82946777
Create Date: 2024-11-10 19:51:15.224449

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "eaf2243d4856"
down_revision = "7d82946777"
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
    # ### end Alembic commands ###

    op.execute(
        """
        INSERT INTO acceso (tipo_usuario, nombre_acceso, ruta, tipo_acceso, estado_reg) VALUES
        ('E', 'Pacientes', '/dashboard/P', 'G', 'V'),
        ('E', 'Medicos', '/dashboard/M', 'G', 'V'),
        ('E', 'Empleados', '/dashboard/M', 'G', 'V'),
        ('E', 'Especialidades', '/especialidades', 'G', 'V'),
        ('E', 'Turnos', '/turnos', 'G', 'V'),
        ('E', 'Fichas', '/fichas', 'G', 'V'),
        ('M', 'Pacientes', '/dashboard/P', 'G', 'V'),
        ('M', 'Turnos', '/turnos', 'V', 'V'),
        ('M', 'Fichas', '/fichas', 'V', 'V'),
        ('P', 'Especialidades', '/especialidades', 'V', 'V'),
        ('p', 'Fichas', '/fichas', 'V', 'V'),
        ('T', 'Pacientes', '/dashboard/P', 'G', 'V'),
        ('T', 'Medicos', '/dashboard/M', 'G', 'V'),
        ('T', 'Empleados', '/dashboard/M', 'G', 'V'),
        ('T', 'Especialidades', '/especialidades', 'G', 'V'),
        ('T', 'Turnos', '/turnos', 'G', 'V'),
        ('T', 'Fichas', '/fichas', 'G', 'V');
        """
    )


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("acceso")
    # ### end Alembic commands ###
