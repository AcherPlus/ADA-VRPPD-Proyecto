import { Component } from '@angular/core';
import { NavbarBipComponent } from "../../navbar-bip/navbar-bip.component";
import { RouterModule } from '@angular/router';

@Component({
    selector: 'app-ver-seguimiento-empresario',
    standalone: true,
    templateUrl: './ver-seguimiento-empresario.component.html',
    styleUrl: './ver-seguimiento-empresario.component.css',
    imports: [NavbarBipComponent, RouterModule]
})
export class VerSeguimientoEmpresarioComponent {

}
