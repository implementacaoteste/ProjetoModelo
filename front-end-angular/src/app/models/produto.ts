// ./src/app/models/produto.model.ts

export class Produto {
    id: number;
    nome: string;
    descricao: string;
    preco: number;
  
    constructor(id?: number, nome?: string, descricao?: string, preco?: number) {
      this.id = id || 0;
      this.nome = nome || '';
      this.descricao = descricao || '';
      this.preco = preco || 0;
    }
  }
  