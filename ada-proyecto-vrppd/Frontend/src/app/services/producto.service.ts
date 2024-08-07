import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ProductoService {

  constructor(private http:HttpClient) { }

  private urlProduct = 'http://127.0.0.1:8000/api/productos/productos/';

  getProductos(): Observable<any>{
    return this.http.get<any>(this.urlProduct);
  }
}
