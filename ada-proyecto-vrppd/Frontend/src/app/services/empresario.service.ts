// empresario.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class EmpresarioService {
  private apiUrl = 'http://127.0.0.1:8000/api/empresarios/empresarios/';
  constructor(private http: HttpClient) {}
  getEmpresarios(): Observable<any> {
    return this.http.get<any>(this.apiUrl);
  }

  login(username: string, password: string): Observable<boolean> {
    return new Observable<boolean>((observer) => {
      this.getEmpresarios().subscribe((empresarios) => {
        const user = empresarios.find(
          (emp: any) =>
            emp.nombre_usuario_emp === username && emp.password_emp === password
        );
        observer.next(!!user);
        observer.complete();
      });
    });
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
