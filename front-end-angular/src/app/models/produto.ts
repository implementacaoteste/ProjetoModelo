// ./src/app/models/produto.model.ts

export class Produto {
    id: number;
    nome: string;
    quantidade: number;
    preco: number;
    ativo: boolean;
  
    constructor(id?: number, nome?: string, preco?: number, quantidade?: number, ativo?: boolean) {
      this.id = id || 0;
      this.nome = nome || '';
      this.quantidade = quantidade || 0;
      this.preco = preco || 0;
      this.ativo = ativo || true;
    }
  }
  