// almacen.service.ts
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AlmacenService {

  
  private urlAlmacen = 'http://127.0.0.1:8000/api/almacenes/almacenes/';
  private urlUbicacion = 'http://127.0.0.1:8000/api/ubicaciones/ubicaciones/';

  constructor(private http: HttpClient) { }

  deleteUbicaciones(id: any): any {
    return this.http.delete<any>(`${this.urlUbicacion}${id}`)
  }

  getUbicaciones(): any {
    return this.http.get<any>(this.urlUbicacion);
  }

  getAlmacenes(): any {
    return this.http.get<any>(this.urlAlmacen);
  }

  postAlmacenes(almacen: any): any {
    return this.http.post<any>(this.urlAlmacen, almacen);
  }

  putAlmacenes(almacen: any): any {
    const id = almacen.idubicacion; // Suponiendo que el almacén tiene un campo 'id'
    return this.http.put<any>(`${this.urlAlmacen}${id}/`, almacen); // Ajusta la URL según tu API
  }
  putUbicaciones(ubicacion: any): any {
    const id = ubicacion.idubicacion; // Suponiendo que la ubicación tiene un campo 'id'
    return this.http.put<any>(`${this.urlUbicacion}${id}/`, ubicacion); // Ajusta la URL según tu API
  }

  postUbicaciones(ubicacion: any): any {
    return this.http.post<any>(this.urlUbicacion, ubicacion);
  }
  deleteAlmacenes(id: any): any {
    return this.http.delete<any>(`${this.urlAlmacen}${id}`);
  }
  


}
