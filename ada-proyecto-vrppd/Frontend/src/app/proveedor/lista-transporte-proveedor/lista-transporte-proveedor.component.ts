import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
import { NavbarBipComponent } from '../../navbar-bip/navbar-bip.component';
@Component({
  selector: 'app-lista-transporte-proveedor',
  standalone: true,
  imports: [RouterModule, NavbarBipComponent],
  templateUrl: './lista-transporte-proveedor.component.html',
  styleUrl: './lista-transporte-proveedor.component.css'
})
export class ListaTransporteProveedorComponent {

}
