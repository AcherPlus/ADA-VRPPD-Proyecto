import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
import { NavbarBipComponent } from '../../navbar-bip/navbar-bip.component';
@Component({
  selector: 'app-editar-productos-proveedor',
  standalone: true,
  imports: [RouterModule, NavbarBipComponent],
  templateUrl: './editar-productos-proveedor.component.html',
  styleUrl: './editar-productos-proveedor.component.css'
})
export class EditarProductosProveedorComponent {

}
