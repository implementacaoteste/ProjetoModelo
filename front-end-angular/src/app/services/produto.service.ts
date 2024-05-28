// ./src/app/services/produto.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';
import { Produto } from '../models/produto';

@Injectable({
  providedIn: 'root'
})
export class ProdutoService {
  private apiUrl = environment.apiUrl;

  constructor(private http: HttpClient) { }

  buscar(texto?: string): Observable<Produto[]> {
    if (texto) {
      return this.http.get<Produto[]>(`${this.apiUrl}?search=${texto}`);
    }
    return this.http.get<Produto[]>(this.apiUrl);
  }

  buscarPorId(id: number): Observable<Produto> {
    return this.http.get<Produto>(`${this.apiUrl}${id}`);
  }

  inserir(produto: Produto): Observable<Produto> {
    return this.http.post<Produto>(this.apiUrl, produto);
  }

  alterar(id: number, produto: Produto): Observable<Produto> {
    return this.http.put<Produto>(`${this.apiUrl}${id}`, produto);
  }

  excluir(id: number): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}${id}`);
  }
}


