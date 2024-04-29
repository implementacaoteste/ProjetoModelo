# app/dal/usuario_dal.py

from flask import jsonify
from app import db
from app.models.usuario import Usuario

class UsuarioDAL:
    def inserir(self, _usuario: Usuario)->Usuario:
        db.session.add(_usuario)
        db.session.commit()
        return _usuario

    def buscar_todos(self):
        return Usuario.query.all()
    
    def buscar_por_id(self, _id: int)->Usuario:
        return Usuario.query.get(_id)
    
    def alterar(self, _usuario: Usuario)->Usuario:
        usuario = self.buscar_por_id(_usuario.id)
        if not usuario:
            return jsonify({'error': 'Usuario não encontrado'}), 404
        usuario.nome_usuario = _usuario.nome_usuario
        usuario.email = _usuario.email
        db.session.commit()
    
    def excluir(self, _id):
        usuario = self.buscar_por_id(_id)
        if not usuario:
            return jsonify({'error': 'Usuário não encontrado'}), 404
        db.session.delete(usuario)
        db.session.commit()