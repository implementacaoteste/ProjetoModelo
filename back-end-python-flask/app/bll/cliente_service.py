from app.dal.cliente_dal import ClienteDAL

class ClienteService:
    @staticmethod
    def listar_clientes():
        return ClienteDAL.listar_clientes()

