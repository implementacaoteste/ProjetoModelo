from app import db
from models.fornecedor import Fornecedor

class FornecedorDAL:
    @staticmethod
    def listar_fornecedores():
        fornecedores = Fornecedor.query.all()
        return [{'id': fornecedor.id, 'nome': fornecedor.nome, 'email': fornecedor.email, 'telefone': fornecedor.telefone} for fornecedor in fornecedores]

    @staticmethod
    def cadastrar_fornecedor(dados):
        fornecedor = Fornecedor(nome=dados['nome'], email=dados['email'], telefone=dados['telefone'])
        db.session.add(fornecedor)
        db.session.commit()
        return {'id': fornecedor.id, 'nome': fornecedor.nome, 'email': fornecedor.email, 'telefone': fornecedor.telefone}

    @staticmethod
    def detalhar_fornecedor(id):
        fornecedor = Fornecedor.query.get(id)
        if fornecedor:
            return {'id': fornecedor.id, 'nome': fornecedor.nome, 'email': fornecedor.email, 'telefone': fornecedor.telefone}
        else:
            return None

    @staticmethod
    def atualizar_fornecedor(id, dados):
        fornecedor = Fornecedor.query.get(id)
        if fornecedor:
            fornecedor.nome = dados['nome']
            fornecedor.email = dados['email']
            fornecedor.telefone = dados['telefone']
            db.session.commit()
            return {'id': fornecedor.id, 'nome': fornecedor.nome, 'email': fornecedor.email, 'telefone': fornecedor.telefone}
        else:
            return None

    @staticmethod
    def deletar_fornecedor(id):
        fornecedor = Fornecedor.query.get(id)
        if fornecedor:
            db.session.delete(fornecedor)
            db.session.commit()
            return True
        else:
            return False
