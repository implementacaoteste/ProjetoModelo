// barra-busca.component.ts

import { Component, Output, EventEmitter, Input } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-barra-busca',
  standalone: true,
  imports: [FormsModule, RouterLink],
  templateUrl: './barra-busca.component.html',
  styleUrl: './barra-busca.component.css'
})
export class BarraBuscaComponent {
  @Input() entidade: string = 'produto';
  @Input() artigo: string = 'o';
  @Output() buscar: EventEmitter<string> = new EventEmitter<string>();
  termoBusca: string = '';

  onBuscar(): void {
    this.buscar.emit(this.termoBusca);
  }
}
