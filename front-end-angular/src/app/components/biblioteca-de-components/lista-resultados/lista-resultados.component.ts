// lista-ListaResultadosComponent.component.ts

import { CommonModule } from '@angular/common';
import { Component, EventEmitter, Input, Output } from '@angular/core';

@Component({
  selector: 'app-lista-resultados',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './lista-resultados.component.html',
  styleUrl: './lista-resultados.component.css'
})
export class ListaResultadosComponent {
  @Input() resultadoList: any[] = [];
  @Input() colunaList: string[] = [];
  @Output() editar: EventEmitter<number> = new EventEmitter<number>();
  @Output() excluir: EventEmitter<number> = new EventEmitter<number>();

  onEditar(id: number): void{
    this.editar.emit(id);
  }

  onExcluir(id: number): void{
    this.excluir.emit(id);
  }
}
