import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class LocalService {

  constructor(private http:HttpClient) { }

  private urlLocal = 'http://127.0.0.1:8000/api/locales/locales/';
  private urlUbicacion = 'http://127.0.0.1:8000/api/ubicaciones/ubicaciones/';
  private urlProducto = 'http://127.0.0.1:8000/api/productos/productos/';

  deleteProductos(id: any): any {
    return this.http.delete<any>(`${this.urlProducto}${id}`)
  }

  getProductos(): any {
    return this.http.get<any>(this.urlProducto);
  }

  postProductos(producto: any): any {
    return this.http.post<any>(this.urlProducto, producto);
  }

  putProductos(producto: any): any {
    const id = producto.idproducto; // Suponiendo que el producto tiene un campo 'id'
    return this.http.put<any>(`${this.urlProducto}${id}/`, producto); // Ajusta la URL según tu API
  }



  deleteUbicaciones(id: any): any {
    return this.http.delete<any>(`${this.urlUbicacion}${id}`)
  }

  getUbicaciones(): any {
    return this.http.get<any>(this.urlUbicacion);
  }

  getLocales(): any {
    return this.http.get<any>(this.urlLocal);
  }

  postLocales(local: any): any {
    return this.http.post<any>(this.urlLocal, local);
  }

  putLocales(local: any): any {
    const id = local.idubicacion; // Suponiendo que el local tiene un campo 'id'
    return this.http.put<any>(`${this.urlLocal}${id}/`, local); // Ajusta la URL según tu API
  }

  putUbicaciones(ubicacion: any): any {
    const id = ubicacion.idubicacion; // Suponiendo que la ubicación tiene un campo 'id'
    return this.http.put<any>(`${this.urlUbicacion}${id}/`, ubicacion); // Ajusta la URL según tu API
  }

  postUbicaciones(ubicacion: any): any {
    return this.http.post<any>(this.urlUbicacion, ubicacion);
  }

  deleteLocales(id: any): any {
    return this.http.delete<any>(`${this.urlLocal}${id}`);
  }

  getLocal(id: any): any {
    return this.http.get<any>(`${this.urlLocal}${id}`);
  }

  getProducto(id: any): any {
    return this.http.get<any>(`${this.urlProducto}${id}`);
  }

  getUbicacion(id: any): any {
    return this.http.get<any>(`${this.urlUbicacion}${id}`);
  }

  getLocalByUbicacion(id: any): any {
    return this.http.get<any>(`${this.urlLocal}?idubicacion=${id}`);
  }

  getUbicacionByLocal(id: any): any {
    return this.http.get<any>(`${this.urlUbicacion}?idlocal=${id}`);
  }

  getLocalByProveedor(id: any): any {
    return this.http.get<any>(`${this.urlLocal}?idproveedor=${id}`);
  }

  getUbicacionByProveedor(id: any): any {
    return this.http.get<any>(`${this.urlUbicacion}?idproveedor=${id}`);
  }

  getLocalByNombre(nombre: any): any {
    return this.http.get<any>(`${this.urlLocal}?nombre=${nombre}`);
  }

  getUbicacionByDireccion(direccion: any): any {
    return this.http.get<any>(`${this.urlUbicacion}?direccion=${direccion}`);
  }

}
