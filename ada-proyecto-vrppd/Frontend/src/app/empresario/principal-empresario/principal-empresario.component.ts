import { Component } from '@angular/core';
import { NavbarBipComponent } from "../../navbar-bip/navbar-bip.component";
import { RouterModule } from '@angular/router';

@Component({
    selector: 'app-principal-empresario',
    standalone: true,
    templateUrl: './principal-empresario.component.html',
    styleUrl: './principal-empresario.component.css',
    imports: [NavbarBipComponent, RouterModule]
})
export class PrincipalEmpresarioComponent {

}
