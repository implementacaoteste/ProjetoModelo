from app.models.shared import db
from app.models.fornecedor import Fornecedor

class FornecedorDAL:
    @staticmethod
    def listar_fornecedores():
        return Fornecedor.query.all()
