# fornecedor_controller.py

from flask import Blueprint, jsonify
from app.bll.fornecedor_service import FornecedorService

bp = Blueprint('fornecedor', __name__)

@bp.route('/fornecedores', methods=['GET'])
def listar_fornecedores():
    # fornecedores = FornecedorService.listar_fornecedores()
    # Converte a lista de fornecedores em um formato JSON e retorna como resposta
    # return jsonify(fornecedores)
    return "Hello, World! This is a test route."

