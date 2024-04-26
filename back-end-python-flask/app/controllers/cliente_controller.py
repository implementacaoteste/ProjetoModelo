from flask import Blueprint, jsonify
from app.bll.cliente_service import ClienteService

bp = Blueprint('cliente', __name__)

@bp.route('/clientes', methods=['GET'])
def listar_clientes():
    clientes = ClienteService.listar_clientes()
    # Converte a lista de clientes em um formato JSON e retorna como resposta
    return jsonify(clientes)
