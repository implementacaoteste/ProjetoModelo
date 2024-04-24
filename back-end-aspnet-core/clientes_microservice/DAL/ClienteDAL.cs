//using Microsoft.EntityFrameworkCore;
using Models;

namespace DAL
{
    public class ClienteDAL
    {
        public void Inserir(Cliente _cliente)
        {
            using (var context = new AppDbContext())
            {
                context.Cliente.Add(_cliente);
                context.SaveChanges();
            }
        }
        public List<Cliente> BuscarTodos()
        {
            using (var context = new AppDbContext())
            {
                return context.Cliente.ToList();
            }
        }
        public Cliente? BuscarPorId(int _id)
        {
            using (var context = new AppDbContext())
            {
                return context.Cliente.FirstOrDefault(u => u.Id == _id);
            }
        }
        public void Alterar(Cliente _cliente)
        {
            using (var context = new AppDbContext())
            {
                context.Entry(_cliente).State = EntityState.Modified;
                context.SaveChanges();
            }
        }
        public void Excluir(int _id)
        {
            using (var context = new AppDbContext())
            {
                var cliente = context.Cliente.Find(_id);
                if (cliente != null)
                {
                    context.Cliente.Remove(cliente);
                    context.SaveChanges();
                }
            }
        }
    }
}