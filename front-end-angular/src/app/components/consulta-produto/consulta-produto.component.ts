// consulta-produto.component.ts

import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { ProdutoService } from '../../services/produto.service';
import { Produto } from '../../models/produto';
import { Router, RouterLink } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { CadastroProdutoComponent } from '../cadastro-produto/cadastro-produto.component';
import { ConfirmacaoExclusaoModalComponent } from '../biblioteca-de-components/confirmacao-exclusao-modal/confirmacao-exclusao-modal.component';
import { BarraBuscaComponent } from '../biblioteca-de-components/barra-busca/barra-busca.component';
import { ListaResultadosComponent } from '../biblioteca-de-components/lista-resultados/lista-resultados.component';

@Component({
  selector: 'app-consulta-produto',
  standalone: true,
  imports: [
    CommonModule,
    CadastroProdutoComponent,
    FormsModule,
    RouterLink,
    ConfirmacaoExclusaoModalComponent,
    BarraBuscaComponent,
    ListaResultadosComponent],
  templateUrl: './consulta-produto.component.html',
  styleUrl: './consulta-produto.component.css'
})
export class ConsultaProdutoComponent {
  resultadoList: Produto[] = [];
  colunaList: string[] =  ['id', 'nome', 'descricao', 'preco'];
  entidade: string = 'produto';
  artigo: string = 'o';
  termoBusca: string = '';
  confirmacaoExclusaoModal: boolean = false;
  produtoParaExcluir: Produto | null = null;
  mensagemRegistroNaoEncontrado: string = '';
  constructor(
    private router: Router,
    private produtoService: ProdutoService
  ) { }
  
  ngOnInit(): void {
    this.onBuscar();
    this.mensagemRegistroNaoEncontrado = '';
  }
  
  onBuscar(termo: string = ''): void {
    this.termoBusca = termo;
    if (this.termoBusca.trim() !== '') {
      this.resultadoList = this.produtoService.buscar(this.termoBusca);
    } else {
      this.resultadoList = this.produtoService.buscar();
    }
    if (this.resultadoList.length === 0) {
      if (this.termoBusca.length > 0) {
        this.mensagemRegistroNaoEncontrado = `Nenhum resultado encontrado para o termo: '${this.termoBusca}'`;
      } else {
        this.mensagemRegistroNaoEncontrado = 'Nenhum registro encontrado';
      }
    } else {
      this.mensagemRegistroNaoEncontrado = '';
    }
  }

  onEditar(id: number): void {
    this.router.navigate(['/cadastro-produto', id]);
  }

  onExcluir(id: number): void {
    this.produtoParaExcluir =  this.produtoService.buscarPorId(id);
    this.confirmacaoExclusaoModal = true;
  }

  onConfirmarExclusao(): void {
    if (this.produtoParaExcluir) {
      this.produtoService.excluir(this.produtoParaExcluir.id);
      this.onBuscar();
      this.onFecharModal();
    }
  }

  onFecharModal(): void {
    this.confirmacaoExclusaoModal = false;
    this.produtoParaExcluir = null;
  }
}

