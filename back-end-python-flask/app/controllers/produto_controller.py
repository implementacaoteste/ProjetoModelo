from flask import Blueprint, jsonify
from app.bll.produto_service import ProdutoService

bp = Blueprint('produto', __name__)

@bp.route('/produtos', methods=['GET'])
def listar_produtos():
    produtos = ProdutoService.listar_produtos()
    # Converte a lista de produtos em um formato JSON e retorna como resposta
    return jsonify(produtos)
