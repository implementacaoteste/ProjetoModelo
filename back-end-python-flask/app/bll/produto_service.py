from app.dal.produto_dal import ProdutoDAL

class ProdutoService:
    @staticmethod
    def listar_produtos():
        return ProdutoDAL.listar_produtos()

