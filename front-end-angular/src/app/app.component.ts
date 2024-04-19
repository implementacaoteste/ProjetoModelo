import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { AppRoutingModule } from './app.routes';
import { NavbarComponent } from './components/navbar/navbar.component';
import { HomeComponent } from './components/home/home.component';
import { CabecalhoComponent } from './components/cabecalho/cabecalho.component';
import { RodaPeComponent } from './components/roda-pe/roda-pe.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [HomeComponent, CabecalhoComponent, RodaPeComponent, NavbarComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'mercearia angular';
}
