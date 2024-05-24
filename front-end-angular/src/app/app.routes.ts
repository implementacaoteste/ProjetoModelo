// ./src/app/app.routes.ts

import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { CadastroProdutoComponent } from './components/cadastro-produto/cadastro-produto.component';
import { ConsultaProdutoComponent } from './components/consulta-produto/consulta-produto.component';
import { CadastroClienteComponent } from './components/cadastro-cliente/cadastro-cliente.component';
import { CadastroFornecedorComponent } from './components/cadastro-fornecedor/cadastro-fornecedor.component';

export const routes: Routes = [
    { path: '', component: HomeComponent },
    { path: 'cadastro-produto', component: CadastroProdutoComponent },
    { path: 'cadastro-produto/:id', component: CadastroProdutoComponent },
    { path: 'consulta-produto', component: ConsultaProdutoComponent },
    { path: 'cadastro-cliente', component: CadastroClienteComponent },
    { path: 'cadastro-fornecedor', component: CadastroFornecedorComponent },
];

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
})
export class AppRoutingModule { }