from flask import request, render_template, url_for, redirect, flash
from flask_login import login_user, logout_user
from ..modelo import Usuario
from . import auth_bp


@auth_bp.route(f"/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        nombreUsuario = request.form.get("nombreUsuario")
        claveUsuairo = request.form.get("claveUsuario")
        recuerdame = request.form.get("recuerdaMe")

        usuario = Usuario.query.filter_by(nombre_usuario=nombreUsuario).first()

        if usuario and usuario.check_password(claveUsuairo):
            tipoE = usuario.tipo_empleado if not None else "E"
            login_user(usuario, recuerdame)
            next = request.args.get("next")
            if next is None or not next.startswith("/"):
                next = url_for("prin.iniciodash", tipo=tipoE)
            return redirect(next)
        else:
            flash("Nombre de Usuario o contraseña incorrecta", "error")

    return render_template("login.html")


@auth_bp.route("/registro")
def retistro():
    return "Registro De usuario"


@auth_bp.route("/logout")
def logout():
    logout_user()
    flash("Hasta otro momento..")
    return redirect(url_for("gral.home"))
