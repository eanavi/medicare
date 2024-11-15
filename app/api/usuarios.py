from flask import jsonify
from .import api_bp
from ..modelo import Usuario

@api_bp.route(f'/usuarios/')
def get_usuarios():
    usuario = Usuario.query.all()
    return jsonify({"usuarios":[usr.to_json() for usr in usuario]})

@api_bp.route(f'/usuario/<int:id>')
def get_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    return jsonify(usuario.to_json())