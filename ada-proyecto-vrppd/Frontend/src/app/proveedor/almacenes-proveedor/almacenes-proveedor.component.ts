import { Component } from '@angular/core';
import { Router, RouterModule } from '@angular/router';
import { NavbarBipComponent } from '../../navbar-bip/navbar-bip.component';
import { AlmacenService } from '../../services/almacen.service';
import { HttpClient } from '@angular/common/http';
import { NgFor } from '@angular/common';
@Component({
  selector: 'app-almacenes-proveedor',
  standalone: true,
  imports: [RouterModule, NavbarBipComponent, NgFor],
  templateUrl: './almacenes-proveedor.component.html',
  styleUrl: './almacenes-proveedor.component.css',
})
export class AlmacenesProveedorComponent {
  constructor(private almacenService: AlmacenService, private router: Router) {}
  ubicaciones: any[] = [];
  ngOnInit(): void {
    this.cargarUbicaciones();
  }
  cargarUbicaciones(): void {
    this.almacenService.getUbicaciones().subscribe(
      (data: any) => {
        this.ubicaciones = data;
      },
      (error: any) => {
        console.error('Error al cargar las ubicaciones', error);
      }
    );
  }

}
