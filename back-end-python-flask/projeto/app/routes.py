# from app import app
# from app.controllers.usuario_controller import *

# # Rotas para usuários
# app.add_url_rule('/usuario', 'inserir_usuario', inserir_usuario, methods=['POST'])
# app.add_url_rule('/usuarios', 'buscar_todos_usuarios', buscar_todos_usuarios, methods=['GET'])
# app.add_url_rule('/usuario/<int:usuario_id>', 'buscar_por_id_usuario', buscar_por_id_usuario, methods=['GET'])
# app.add_url_rule('/usuario/<int:usuario_id>', 'alterar_usuario', alterar_usuario, methods=['PUT'])
# app.add_url_rule('/usuario/<int:usuario_id>', 'excluir_usuario', excluir_usuario, methods=['DELETE'])



# from app import app, db
# from flask import request, jsonify
# from app.models.usuario import Usuario

# # Rota para criar um novo usuário
# @app.route('/usuario', methods=['POST'])
# def inserir_usuario():
#     data = request.json
#     nome_usuario = data.get('nome_usuario')
#     email = data.get('email')
#     if not nome_usuario or not email:
#         return jsonify({'error': 'nome_usuario and email are required'}), 400
#     novo_usuario = Usuario(nome_usuario=nome_usuario, email=email)
#     db.session.add(novo_usuario)
#     db.session.commit()
#     return jsonify({'message': 'Usuário inserido com sucesso!'}), 201

# # Rota para obter todos os usuários
# @app.route('/usuarios', methods=['GET'])
# def buscar_todos_usuarios():
#     usuarios = Usuario.query.all()
#     dados_usuarios = [{'id': usuario.id, 'nome_usuario': usuario.nome_usuario, 'email': usuario.email} for usuario in usuarios]
#     return jsonify(dados_usuarios)

# # Rota para obter um usuário pelo ID
# @app.route('/usuario/<int:usuario_id>', methods=['GET'])
# def buscar_por_id_usuario(usuario_id):
#     usuario = Usuario.query.get(usuario_id)
#     if not usuario:
#         return jsonify({'error': 'Usuário não encontrado'}), 404
#     dados_usuarios = {'id': usuario.id, 'nome_usuario': usuario.nome_usuario, 'email': usuario.email}
#     return jsonify(dados_usuarios)

# # Rota para atualizar um usuário pelo ID
# @app.route('/usuario/<int:usuario_id>', methods=['PUT'])
# def alterar_usuario(usuario_id):
#     data = request.json
#     usuario = Usuario.query.get(usuario_id)
#     if not usuario:
#         return jsonify({'error': 'Usuario não encontrado'}), 404
#     usuario.nome_usuario = data.get('nome_usuario', usuario.nome_usuario)
#     usuario.email = data.get('email', usuario.email)
#     db.session.commit()
#     return jsonify({'message': 'Usuário atualizado com sucesso!'})

# # Rota para excluir um usuário pelo ID
# @app.route('/usuario/<int:usuario_id>', methods=['DELETE'])
# def excluir_usuario(usuario_id):
#     usuario = Usuario.query.get(usuario_id)
#     if not usuario:
#         return jsonify({'error': 'Usuário não encontrado'}), 404
#     db.session.delete(usuario)
#     db.session.commit()
#     return jsonify({'message': 'Usuário excluído com sucesso!'})


# def inserir_dados_iniciais():
#     # Verifica se já existem usuários no banco de dados
#     with app.app_context():
#         if Usuario.query.count() == 0:
#             # Adiciona usuários de exemplo
#             usuario1 = Usuario(nome_usuario='adm', email='adm@example.com')
#             usuario2 = Usuario(nome_usuario='teste', email='teste@example.com')

#             # Adiciona os usuários ao banco de dados
#             db.session.add(usuario1)
#             db.session.add(usuario2)

#             # Comita as mudanças ao banco de dados
#             db.session.commit()
#             print('Dados iniciais adicionados com sucesso.')
#         else:
#             print('Já existem dados no banco de dados.')
