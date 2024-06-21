import { Component } from '@angular/core';
import { NavbarBipComponent } from "../../navbar-bip/navbar-bip.component";
import { RouterModule } from '@angular/router';

@Component({
    selector: 'app-envio-input-empresario',
    standalone: true,
    templateUrl: './envio-input-empresario.component.html',
    styleUrl: './envio-input-empresario.component.css',
    imports: [NavbarBipComponent, RouterModule]
})
export class EnvioInputEmpresarioComponent {

}
