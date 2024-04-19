// confirmacao-exclusao-modal.component.ts

import { CommonModule } from '@angular/common';
import { Component, EventEmitter, Input, Output } from '@angular/core';

@Component({
  selector: 'app-confirmacao-exclusao-modal',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './confirmacao-exclusao-modal.component.html',
  styleUrl: './confirmacao-exclusao-modal.component.css'
})
export class ConfirmacaoExclusaoModalComponent {
  @Input() entidade: string = 'item';
  @Input() artigo: string = 'o';
  @Input() titulo: string = 'Confirmar exclusão';
  @Input() modalAberto: boolean = false;
  @Output() cancelar: EventEmitter<void> = new EventEmitter<void>();
  @Output() confirmar: EventEmitter<void> = new EventEmitter<void>();

  fecharModal(): void {
    this.cancelar.emit();
  }

  confirmarExclusao(): void {
    this.confirmar.emit();
  }

  get mensagem(): string {
    return `Tem certeza de que deseja excluir est${this.artigo === 'o' ? 'e' : 'a'} ${this.entidade}?`;
  }
}
