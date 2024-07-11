// auth.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private apiUrl = 'http://127.0.0.1:8000/api/proveedores/proveedores/1';

  constructor(private http: HttpClient) { }

  login(nombreUsuario: string, password: string): Observable<boolean> {
    return this.http.get<any>(this.apiUrl).pipe(
      map(user => user.nombre_usuario_prov === nombreUsuario && user.password_prov === password)
    );
  }

  isLoggedIn(): boolean {
    return !!localStorage.getItem('isLoggedIn');
  }

  setLoginStatus(status: boolean): void {
    localStorage.setItem('isLoggedIn', status ? 'true' : 'false');
  }

  logout(): void {
    localStorage.removeItem('isLoggedIn');
  }
}
