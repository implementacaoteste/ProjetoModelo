// ./src/app/app.config.ts

import { ApplicationConfig } from '@angular/core';
import { provideRouter } from '@angular/router';
import { routes } from './app.routes';

// Importar componentes
import { AppComponent } from './app.component';
import { CadastroProdutoComponent } from './components/cadastro-produto/cadastro-produto.component';
import { MensagemCRUDComponent } from './components/biblioteca-de-components/mensagem-crud/mensagem-crud.component';
import { BarraBuscaComponent } from './components/biblioteca-de-components/barra-busca/barra-busca.component';
import { ListaResultadosComponent } from './components/biblioteca-de-components/lista-resultados/lista-resultados.component';
import { ConfirmacaoExclusaoModalComponent } from './components/biblioteca-de-components/confirmacao-exclusao-modal/confirmacao-exclusao-modal.component';

export const appConfig: ApplicationConfig = {
  providers: [
    provideRouter(routes)
  ]
};
