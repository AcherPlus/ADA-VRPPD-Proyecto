import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
import { NavbarBipComponent } from '../../navbar-bip/navbar-bip.component';
@Component({
  selector: 'app-almacenes-proveedor',
  standalone: true,
  imports: [RouterModule, NavbarBipComponent],
  templateUrl: './almacenes-proveedor.component.html',
  styleUrl: './almacenes-proveedor.component.css'
})
export class AlmacenesProveedorComponent {

}
