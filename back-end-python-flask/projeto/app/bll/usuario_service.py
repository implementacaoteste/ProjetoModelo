# app/bll/usuario_service.py

from typing import List
from flask import jsonify
from app.models.usuario import Usuario
from app.dal.usuario_dal import UsuarioDAL

usuario_dal = UsuarioDAL()

class UsuarioService:
    def inserir(self, _usuario: Usuario)->Usuario:
        return usuario_dal.inserir(_usuario)

    def buscar_todos(self) -> List[Usuario]:
        return usuario_dal.buscar_todos()
    
    def buscar_por_id(self, _id: int)->Usuario:
        return usuario_dal.buscar_por_id(_id)
    
    def altearar(self, _usuario: Usuario)->Usuario:
        return usuario_dal.alterar(_usuario)
    
    def excluir(self, _id):
        usuario_dal.excluir(_id)