// cadastro-produto.component.html

import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Produto } from '../../models/produto';
import { ProdutoService } from '../../services/produto.service';
import { ActivatedRoute, Route } from '@angular/router';
import { Router } from '@angular/router';
import { MensagemCRUDComponent } from '../biblioteca-de-components/mensagem-crud/mensagem-crud.component';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-cadastro-produto',
  standalone: true,
  imports: [
    FormsModule,
    CommonModule,
    MensagemCRUDComponent,
  ],
  templateUrl: './cadastro-produto.component.html',
  styleUrl: './cadastro-produto.component.css'
})
export class CadastroProdutoComponent {
  novoProduto: Produto = new Produto();
  botaoAcao: string = 'Salvar';
  letraDoCRUD: string = 'C';
  tipoMensagem: 'sucesso' | 'erro' | 'aviso' = 'sucesso';
  mensagem: string | null = null;
  nomeEntidade: string = 'O produto';

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
    this.mensagem = 'asdfe';
  }
  
  exibirMensagem(mensagem?: string): void {
    mensagem = 'Registro salvo com sucesso!'
  }
  
  onConfirmarMensagem(): void {
    this.mensagem = null;
    this.router.navigate(['/consulta-produto']);
  }
}


