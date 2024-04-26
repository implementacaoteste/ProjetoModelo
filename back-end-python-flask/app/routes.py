from app import app
from flask import request, jsonify
#from models.fornecedor import Fornecedor
#from bll.fornecedor_service import FornecedorService

@app.route('/fornecedores', methods=['GET'])
def listar_fornecedores():
    fornecedores = [] # FornecedorService.listar_fornecedores()
    return jsonify(fornecedores)


# # routes.py

# from flask import Blueprint
# from app.controllers import fornecedor_controller # , cliente_controller, produto_controller

# bp = Blueprint('routes', __name__)

# # # Rotas para fornecedores
# # bp.register_blueprint(fornecedor_controller.bp)

# # # Rotas para clientes
# # bp.register_blueprint(cliente_controller.bp)

# # # Rotas para produtos
# # bp.register_blueprint(produto_controller.bp)
