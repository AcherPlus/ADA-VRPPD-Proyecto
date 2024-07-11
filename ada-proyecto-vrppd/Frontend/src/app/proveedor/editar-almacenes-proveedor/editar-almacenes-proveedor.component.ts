import { Component, OnInit } from '@angular/core';
import { Router, RouterModule } from '@angular/router';
import { NavbarBipComponent } from '../../navbar-bip/navbar-bip.component';
import { AlmacenService } from '../../services/almacen.service';
import { NgFor } from '@angular/common';

// Extend jQuery to include the 'modal' method
declare global {
  interface JQuery {
    modal(action: string): JQuery;
  }
}
@Component({
  selector: 'app-editar-almacenes-proveedor',
  standalone: true,
  imports: [RouterModule, NavbarBipComponent, NgFor],
  templateUrl: './editar-almacenes-proveedor.component.html',
  styleUrls: ['./editar-almacenes-proveedor.component.css'],
})
export class EditarAlmacenesProveedorComponent implements OnInit {
  ubicaciones: any[] = []; // Aquí se almacenarán las ubicaciones obtenidas
  seleccionados: any[] = []; // Para almacenar las ubicaciones seleccionadas para eliminar o editar
  ubicacionSeleccionada: any; // Para almacenar la ubicación que se va a eliminar

  constructor(private almacenService: AlmacenService, private router: Router) {}

  ngOnInit(): void {
    this.cargarUbicaciones();
  }

  cargarUbicaciones(): void {
    this.almacenService.getUbicaciones().subscribe(
      (data: any) => {
        this.ubicaciones = data; // Cargar la lista de ubicaciones desde el servicio
      },
      (error: any) => {
        console.error('Error al cargar las ubicaciones', error);
      }
    );
  }

  agregarUbicacion(): void {
    // Implementar lógica para agregar una ubicación
    const nuevaUbicacion = {
      direccion: 'Nueva dirección',
      distrito: 'Nuevo distrito',
      region: 'Nueva región',
      longitud: 0.0,
      latitud: 0.0
    };
    this.almacenService.postUbicaciones(nuevaUbicacion).subscribe(
      (data: any) => {
        console.log('Ubicación agregada correctamente', data);
        this.cargarUbicaciones(); // Recargar la lista después de agregar
      },
      (error: any) => {
        console.error('Error al agregar la ubicación', error);
        // Manejar el error aquí
      }
    );
  }

  
}