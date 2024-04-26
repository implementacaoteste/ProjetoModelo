from app.models import db, Produto

class ProdutoDAL:
    @staticmethod
    def listar_produtos():
        return Produto.query.all()
