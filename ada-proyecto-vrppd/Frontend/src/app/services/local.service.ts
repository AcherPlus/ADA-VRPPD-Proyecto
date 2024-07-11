import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class LocalService {
  constructor(private http: HttpClient) {}

  private urlLocal = 'http://127.0.0.1:8000/api/locales/locales/';

  getLocales(): Observable<any> {
    return this.http.get<any>(this.urlLocal);
  }

  addLocal(local: any): Observable<any> {
    return this.http.post<any>(this.urlLocal, local);
  }
}
