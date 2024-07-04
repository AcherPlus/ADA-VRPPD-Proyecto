import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
import { NavbarBipComponent } from '../../navbar-bip/navbar-bip.component';
@Component({
  selector: 'app-productos-proveedor',
  standalone: true,
  imports: [RouterModule, NavbarBipComponent],
  templateUrl: './productos-proveedor.component.html',
  styleUrl: './productos-proveedor.component.css'
})
export class ProductosProveedorComponent {

}
