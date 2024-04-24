using BLL;
//using Infra;
using Models;
using Newtonsoft.Json;
using Microsoft.AspNetCore.Mvc;

namespace API.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class ClienteController : ControllerBase
    {
        [HttpPost]
        public IActionResult Inserir(Cliente _cliente)
        {
            string erro;
            if (_cliente == null)
            {
                erro = Texto.Verbose(nameof(Cliente), Mensagem.EntidadeNula);
                Log.GravarLog($"Erro: {this.GetType().Name} | {erro}");
                return BadRequest(erro);
            }

            try
            {
                new ClienteBLL().Inserir(_cliente);
                return CreatedAtAction(nameof(BuscarPorId), new { _id = _cliente.Id }, _cliente);
            }
            catch (Exception ex)
            {
                erro = Texto.Verbose(nameof(Cliente), Mensagem.Erro500);
                Log.GravarLog($"Erro: {this.GetType().Name} | {erro}: {ex.Message}");
                return StatusCode(500, $"{erro}");
            }
        }
        [HttpGet]
        public IActionResult BuscarTodos()
        {
            Log.GravarLog($"Buscando todos os registros de {Texto.Verbose(nameof(Cliente)).ToLower()}.");
            string erro;
            try
            {
                var clienteList = new ClienteBLL().BuscarTodos();

                if (clienteList == null || clienteList.Count == 0)
                {
                    erro = Texto.Verbose(nameof(Cliente), Mensagem.NaoEncontrado);
                    return NotFound(erro);
                }
                Log.GravarLog($"Resultado: {JsonConvert.SerializeObject(clienteList)}");
                return Ok(clienteList);
            }
            catch (Exception ex)
            {
                erro = Texto.Verbose(nameof(Cliente), Mensagem.Erro500);
                Log.GravarLog($"Erro: {this.GetType().Name} | {erro}: {ex.Message}");
                return StatusCode(500, $"{erro}");
            }
        }
        [HttpGet("{_id}")]
        public IActionResult BuscarPorId(int _id)
        {
            Log.GravarLog($"Buscando registro de {Texto.Verbose(nameof(Cliente)).ToLower()} por id: {_id}");
            string erro;
            try
            {
                var cliente = new ClienteBLL().BuscarPorId(_id);

                if (cliente == null)
                {
                    erro = Texto.Verbose(nameof(Cliente), Mensagem.NaoEncontrado);
                    return NotFound(erro);
                }
                Log.GravarLog($"Resultado: {JsonConvert.SerializeObject(cliente)}");
                return Ok(cliente);
            }
            catch (Exception ex)
            {
                erro = Texto.Verbose(nameof(Cliente), Mensagem.Erro500);
                Log.GravarLog($"Erro: {this.GetType().Name} | {erro}: {ex.Message}");
                return StatusCode(500, $"{erro}");
            }
        }
        [HttpPut("{_id}")]
        public IActionResult Alterar(int _id, Cliente _cliente)
        {
            Log.GravarLog($"Alterando registro de {Texto.Verbose(nameof(Cliente))}: {JsonConvert.SerializeObject(_cliente)}");
            string erro;
            try
            {
                new ClienteBLL().Alterar(_cliente);
                Log.GravarLog($"Registro de {Texto.Verbose(nameof(Cliente))} alterado com sucesso.");
                return NoContent();
            }
            catch (Exception ex)
            {
                erro = Texto.Verbose(nameof(Cliente), Mensagem.Erro500);
                Log.GravarLog($"Erro: {this.GetType().Name} | {erro}: {ex.Message}");
                return StatusCode(500, $"{erro}");
            }
        }
        [HttpDelete("{_id}")]
        public IActionResult Excluir(int _id)
        {
            Log.GravarLog($"Excluindo registro de {Texto.Verbose(nameof(Cliente))}: {_id}");
            string erro;
            try
            {
                new ClienteBLL().Excluir(_id);
                Log.GravarLog($"Registro de {Texto.Verbose(nameof(Cliente))} excluído com sucesso: {_id}");
                return NoContent();
            }
            catch (Exception ex)
            {
                erro = Texto.Verbose(nameof(Cliente), Mensagem.Erro500);
                Log.GravarLog($"Erro: {this.GetType().Name} | {erro}: {ex.Message}");
                return StatusCode(500, $"{erro}");
            }
        }
    }
}