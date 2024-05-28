// ./src/app/app.module.ts

import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { AppRoutingModule } from './app.routes';
import { MensagemCRUDComponent } from './components/biblioteca-de-components/mensagem-crud/mensagem-crud.component';
import { HomeComponent } from './components/home/home.component';
// Importe outros componentes e serviços necessários aqui

@NgModule({
  declarations: [
    AppComponent,
    MensagemCRUDComponent,
    HomeComponent,
    // Liste outros componentes aqui
  ],
  imports: [
    BrowserModule,
    RouterModule,
    FormsModule,
    HttpClientModule,
    AppRoutingModule,
    // Importe outros módulos necessários aqui
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }


