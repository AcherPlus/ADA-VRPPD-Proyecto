import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
import { NavbarBipComponent } from '../../navbar-bip/navbar-bip.component';
@Component({
  selector: 'app-bienvenido-proveedor',
  standalone: true,
  imports: [RouterModule, NavbarBipComponent],
  templateUrl: './bienvenido-proveedor.component.html',
  styleUrl: './bienvenido-proveedor.component.css'
})
export class BienvenidoProveedorComponent {

}
