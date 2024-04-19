// feedback-message.component.ts

import { CommonModule } from '@angular/common';
import { Component, EventEmitter, Input, Output, output } from '@angular/core';
import { endWith } from 'rxjs';

@Component({
  selector: 'app-mensagem-crud',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './mensagem-crud.component.html',
  styleUrl: './mensagem-crud.component.css'
})
export class MensagemCRUDComponent {
  @Input() tipo: 'sucesso' | 'erro' | 'aviso' = 'sucesso';
  @Input() nomeEntidade: string = 'O registro';
  @Input() letraDoCRUD: string = 'C';
  @Input() mensagem: string | null = null;
  @Output() confirmar: EventEmitter<void> = new EventEmitter<void>();

  getMensagem() {
    if (this.tipo === 'sucesso') {
      if (this.letraDoCRUD === 'C') {
        return `${this.nomeEntidade} foi salvo com sucesso!`;
      } else if (this.letraDoCRUD === 'U') {
        return `${this.nomeEntidade} foi atualizado com sucesso!`;
      } else if (this.letraDoCRUD === 'D') {
        return `${this.nomeEntidade} foi excluído com sucesso!`;
      }
    }

    if (this.tipo === 'erro') {
      if (this.letraDoCRUD === 'C') {
        return `Ocorreu um erro ao tentar salvar ${this.nomeEntidade.toLowerCase()}!`;
      } else if (this.letraDoCRUD === 'U') {
        return `Ocorreu um erro ao tentar atualizar ${this.nomeEntidade.toLowerCase()}!`;
      } else if (this.letraDoCRUD === 'D') {
        return `Ocorreu um erro ao tentar excluir ${this.nomeEntidade.toLowerCase()}!`;
      }
    }

    return this.mensagem;
  }

  getModalTitulo(): string {
    return this.tipo === 'sucesso' ? 'Sucesso' : 'Erro';
  }

  onFecharModal(): void {
    this.confirmar.emit();
  }
}
