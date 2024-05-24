// ./src/app/components/cadastro-produto/cadastro-produto.component.html

import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { ProdutoService } from '../../services/produto.service';
import { MensagemCRUDComponent } from '../biblioteca-de-components/mensagem-crud/mensagem-crud.component';
import { ActivatedRoute, Route } from '@angular/router';
@Component({
  selector: 'app-cadastro-produto',
  standalone: true,
  templateUrl: './cadastro-produto.component.html',
  imports: [FormsModule, MensagemCRUDComponent, Route],
  styleUrls: ['./cadastro-produto.component.css']
})
export class CadastroProdutoComponent {
  // Declaração de variáveis
  novoProduto: any = {
    nome: '',
    descricao: '',
    preco: 0
  };
  tipoMensagem: 'sucesso' | 'erro' | 'aviso' = 'sucesso';
  nomeEntidade: string = 'Produto';
  botaoAcao: string = 'Salvar';
  mensagem: string = '';
  letraDoCRUD: string = 'C';

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private produtoService: ProdutoService
  ) { };

  ngOnInit(): void {
    const idParam = this.route.snapshot.paramMap.get('id');

    if (idParam != null) {
      this.letraDoCRUD = 'U';
      const id = +idParam
      if (id) {
        this.novoProduto = this.produtoService.buscarPorId(id);
        this.botaoAcao = 'Atualizar';
      }
    }
  }

  salvar(): void {
    if (this.botaoAcao === 'Salvar') 
      this.produtoService.inserir(this.novoProduto);
    else 
      this.produtoService.atualizar(this.novoProduto.id, this.novoProduto);

      this.tipoMensagem = 'sucesso';
      this.mensagem = 'Produto salvo com sucesso!';
  }

  limparFormulario() {
    this.novoProduto = {
      nome: '',
      descricao: '',
      preco: 0
    };
    this.mensagem = '';
  }

  // Lógica para editar um produto (exemplo)
  editarProduto(produto: any) {
    this.novoProduto = { ...produto };
    this.botaoAcao = 'Atualizar';
  }

  // Lógica para cancelar a edição
  cancelarEdicao() {
    this.limparFormulario();
    this.botaoAcao = 'Salvar';
  }
}


