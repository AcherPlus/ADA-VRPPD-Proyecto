import { Component } from '@angular/core';
import { NavbarBipComponent } from "../../navbar-bip/navbar-bip.component";
import { RouterModule } from '@angular/router';

@Component({
    selector: 'app-envio-resumen-empresario',
    standalone: true,
    templateUrl: './envio-resumen-empresario.component.html',
    styleUrl: './envio-resumen-empresario.component.css',
    imports: [NavbarBipComponent, RouterModule]
})
export class EnvioResumenEmpresarioComponent {

}
