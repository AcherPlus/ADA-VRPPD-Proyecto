import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
import { NavbarBipComponent } from '../../navbar-bip/navbar-bip.component';
@Component({
  selector: 'app-historial-proveedor',
  standalone: true,
  imports: [RouterModule, NavbarBipComponent],
  templateUrl: './historial-proveedor.component.html',
  styleUrl: './historial-proveedor.component.css'
})
export class HistorialProveedorComponent {

}
