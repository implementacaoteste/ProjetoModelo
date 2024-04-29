# __init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://SUPORTE:2@19SurfOnline@database/SIM'  # URI do banco de dados MySQL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

def inserir_dados_iniciais():
    # Verifica se já existem usuários no banco de dados
    if Usuario.query.count() == 0:
        # Adiciona usuários de exemplo
        usuario1 = Usuario(nome_usuario='adm', email='adm@example.com')
        usuario2 = Usuario(nome_usuario='teste', email='teste@example.com')
        # Adiciona os usuários ao banco de dados
        db.session.add(usuario1)
        db.session.add(usuario2)
        # Comita as mudanças ao banco de dados
        db.session.commit()
        print('Dados iniciais adicionados com sucesso.')
    else:
        print('Já existem dados no banco de dados.')

from app.controllers.usuario_controller import *  # Importa todas as rotas da controller de usuários