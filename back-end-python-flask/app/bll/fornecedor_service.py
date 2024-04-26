from dal.fornecedor_dal import FornecedorDAL

class FornecedorService:
    @staticmethod
    def listar_fornecedores():
        return FornecedorDAL.listar_fornecedores()

    @staticmethod
    def cadastrar_fornecedor(dados):
        return FornecedorDAL.cadastrar_fornecedor(dados)

    @staticmethod
    def detalhar_fornecedor(id):
        return FornecedorDAL.detalhar_fornecedor(id)

    @staticmethod
    def atualizar_fornecedor(id, dados):
        return FornecedorDAL.atualizar_fornecedor(id, dados)

    @staticmethod
    def deletar_fornecedor(id):
        return FornecedorDAL.deletar_fornecedor(id)
