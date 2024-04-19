// produto.service.ts

import { Injectable } from '@angular/core';
import { Produto } from '../models/produto';

@Injectable({
  providedIn: 'root'
})
export class ProdutoService {
  private produtos: Produto[] = [];

  constructor() { }

  buscar(texto?: string): Produto[] {
    if (texto) {
      return this.produtos.filter(p => p.nome.toLowerCase().includes(texto.toLowerCase()));
    }
    return this.produtos;
  }

  buscarPorId(id: number): Produto {
    return this.produtos.filter(p => p.id === id)[0];
  }

  inserir(produto: Produto): void {
    produto.id = this.produtos.length + 1;
    this.produtos.push(produto);
  }

  atualizar(id: number, novoProduto: Produto): void {
    const index = this.produtos.findIndex(p => p.id == id);
    if (index !== -1)
      this.produtos[index] = novoProduto;
  }

  excluir(id: number): void {
    this.produtos = this.produtos.filter(p => p.id !== id);
  }
}


