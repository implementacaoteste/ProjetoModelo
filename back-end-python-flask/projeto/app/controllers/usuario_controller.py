# app/controllers/usuario_controller.py

from app import app
from flask import request, jsonify
from app.models.usuario import Usuario
from app.bll.usuario_service import UsuarioService

usuario_service = UsuarioService()

# Rota para criar um novo usuário
@app.route('/usuario', methods=['POST'])
def inserir():
    data = request.json
    nome_usuario = data.get('nome_usuario')
    email = data.get('email')
    if not nome_usuario or not email:
        return jsonify({'error': 'nome_usuario and email are required'}), 400
    usuario = Usuario(nome_usuario=nome_usuario, email=email)
    usuario = usuario_service.inserir(usuario)
    return jsonify({'message': 'Usuário inserido com sucesso!'}), 201

# Rota para obter todos os usuários
@app.route('/usuarios', methods=['GET'])
def buscar_todos():
    resultado = usuario_service.buscar_todos()
    usuarioList = [{'id': usuario.id, 'nome_usuario': usuario.nome_usuario, 'email': usuario.email} for usuario in resultado]
    return jsonify(usuarioList)

# Rota para obter um usuário pelo ID
@app.route('/usuario/<int:usuario_id>', methods=['GET'])
def buscar_por_id(usuario_id):
    usuario = usuario_service.buscar_por_id(usuario_id)
    if not usuario:
        return jsonify({'error': 'Usuário não encontrado'}), 404
    dados_usuario = {'id': usuario.id, 'nome_usuario': usuario.nome_usuario, 'email': usuario.email}
    return jsonify(dados_usuario)

# Rota para atualizar um usuário pelo ID
@app.route('/usuario/<int:usuario_id>', methods=['PUT'])
def alterar(usuario_id):
    usuario = Usuario()
    data = request.json
    usuario.nome_usuario = data.get('nome_usuario')
    usuario.email = data.get('email')
    if not usuario.nome_usuario or not usuario.email:
        return jsonify({'error': 'nome_usuario e email são obrigatórios'}), 400
    
    usuario_service.altearar(usuario)

    return jsonify({'message': 'Usuário atualizado com sucesso!'})

# Rota para excluir um usuário pelo ID
@app.route('/usuario/<int:usuario_id>', methods=['DELETE'])
def excluir(usuario_id):
    usuario_service.excluir(usuario_id)
    return jsonify({'message': 'Usuário excluído com sucesso!'})