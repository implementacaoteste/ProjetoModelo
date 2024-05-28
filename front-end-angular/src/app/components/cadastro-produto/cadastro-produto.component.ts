// ./src/app/components/cadastro-produto/cadastro-produto.component.html

import { Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { ProdutoService } from '../../services/produto.service';
import { MensagemCRUDComponent } from '../biblioteca-de-components/mensagem-crud/mensagem-crud.component';
import { ActivatedRoute } from '@angular/router';
import { CommonModule } from '@angular/common';
import { Produto } from '../../models/produto';

@Component({
  selector: 'app-cadastro-produto',
  standalone: true,
  templateUrl: './cadastro-produto.component.html',
  imports: [CommonModule, FormsModule, MensagemCRUDComponent],
  styleUrls: ['./cadastro-produto.component.css']
})
export class CadastroProdutoComponent implements OnInit {
  novoProduto: Produto = {
    id: 0,
    nome: '',
    preco: 0,
    quantidade: 0,
    ativo: true
  };
  tipoMensagem: 'sucesso' | 'erro' | 'aviso' = 'sucesso';
  nomeEntidade: string = 'Produto';
  botaoAcao: string = 'Salvar';
  mensagem: string = '';
  letraDoCRUD: string = 'C';

  constructor(
    private route: ActivatedRoute,
    private produtoService: ProdutoService
  ) { }

  ngOnInit(): void {
    const idParam = this.route.snapshot.paramMap.get('id');

    if (idParam != null) {
      this.letraDoCRUD = 'U';
      const id = +idParam;
      if (id) {
        this.produtoService.buscarPorId(id).subscribe(produto => {
          this.novoProduto = produto;
          this.botaoAcao = 'Atualizar';
        });
      }
    }
  }

  salvar(): void {
    if (this.botaoAcao === 'Salvar') {
      this.produtoService.inserir(this.novoProduto).subscribe(() => {
        this.tipoMensagem = 'sucesso';
        this.mensagem = 'Produto salvo com sucesso!';
        this.limparFormulario();
      });
    } else {
      this.produtoService.alterar(this.novoProduto.id, this.novoProduto).subscribe(() => {
        this.tipoMensagem = 'sucesso';
        this.mensagem = 'Produto atualizado com sucesso!';
        this.limparFormulario();
      });
    }
  }

  limparFormulario() {
    this.novoProduto = {
      id: 0,
      nome: '',
      preco: 0,
      quantidade: 0,
      ativo: true
    };
    this.mensagem = '';
  }

  editarProduto(produto: Produto) {
    this.novoProduto = { ...produto };
    this.botaoAcao = 'Atualizar';
  }

  cancelarEdicao() {
    this.limparFormulario();
    this.botaoAcao = 'Salvar';
  }
}



