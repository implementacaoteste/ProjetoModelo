using DAL;
using Models;

namespace BLL
{
    public class ClienteBLL
    {
        private void ValidarDados(Cliente _cliente, bool _estaInserindo = true)
        {
            // if (_cliente == null)
            //     throw new Exception("Informe cliente.");
            // if (!_estaInserindo && _cliente.Id <= 0)
            //     throw new Exception("O id tem que ser maior que 0 (zero)");
        }
        public void Inserir(Cliente _cliente)
        {
            // ValidarDados(_cliente);
            // new ClienteDAL().Inserir(_cliente);
        }
        public List<Cliente> BuscarTodos()
        {
            return new List<Cliente>();
        }
        public Cliente? BuscarPorId(int _id)
        {
            return new Cliente();
        }
        public void Alterar(Cliente _cliente)
        {
            // ValidarDados(_cliente, false);
            // new ClienteDAL().Alterar(_cliente);
        }
        public void Excluir(int _id)
        {
            // new ClienteDAL().Excluir(_id);
        }
    }
}