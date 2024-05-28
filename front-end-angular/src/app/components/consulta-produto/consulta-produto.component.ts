// ./src/components/consulta-produto/consulta-produto.component.ts

import { Component, OnInit } from '@angular/core';
import { ProdutoService } from '../../services/produto.service';
import { Produto } from '../../models/produto';
import { Router } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { BarraBuscaComponent,  } from '../biblioteca-de-components/barra-busca/barra-busca.component';
import { ListaResultadosComponent } from '../biblioteca-de-components/lista-resultados/lista-resultados.component';
import { ConfirmacaoExclusaoModalComponent } from '../biblioteca-de-components/confirmacao-exclusao-modal/confirmacao-exclusao-modal.component';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-consulta-produto',
  templateUrl: './consulta-produto.component.html',
  standalone: true,
  imports: [FormsModule, BarraBuscaComponent, ListaResultadosComponent, ConfirmacaoExclusaoModalComponent, CommonModule],
  styleUrls: ['./consulta-produto.component.css']
})
export class ConsultaProdutoComponent implements OnInit {
  resultadoList: Produto[] = [];
  colunaList: string[] =  ['id', 'nome', 'quantidade', 'preco'];
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
  }
  
  onBuscar(termo: string = ''): void {
    this.termoBusca = termo;
    this.produtoService.buscar(this.termoBusca).subscribe(
      (produtos: Produto[]) => {
        this.resultadoList = produtos;
        if (this.resultadoList.length === 0) {
          if (this.termoBusca.length > 0) {
            this.mensagemRegistroNaoEncontrado = `Nenhum resultado encontrado para o termo: '${this.termoBusca}'`;
          } else {
            this.mensagemRegistroNaoEncontrado = 'Nenhum registro encontrado';
          }
        } else {
          this.mensagemRegistroNaoEncontrado = '';
        }
      },
      (error) => {
        console.error('Erro ao buscar produtos:', error);
      }
    );
  }

  onEditar(id: number): void {
    this.router.navigate(['/cadastro-produto', id]);
  }

  onExcluir(id: number): void {
    this.produtoService.buscarPorId(id).subscribe(
      (produto: Produto) => {
        this.produtoParaExcluir = produto;
        this.confirmacaoExclusaoModal = true;
      },
      (error) => {
        console.error('Erro ao buscar produto:', error);
      }
    );
  }

  onConfirmarExclusao(): void {
    if (this.produtoParaExcluir) {
      this.produtoService.excluir(this.produtoParaExcluir.id).subscribe(
        () => {
          this.onBuscar();
          this.onFecharModal();
        },
        (error) => {
          console.error('Erro ao excluir produto:', error);
        }
      );
    }
  }

  onFecharModal(): void {
    this.confirmacaoExclusaoModal = false;
    this.produtoParaExcluir = null;
  }
}


