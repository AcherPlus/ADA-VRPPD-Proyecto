import { Component } from '@angular/core';
import { NavbarBipComponent } from "../../navbar-bip/navbar-bip.component";
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-administrar-local',
  standalone: true,
  imports: [NavbarBipComponent, RouterModule],
  templateUrl: './administrar-local.component.html',
  styleUrl: './administrar-local.component.css'
})
export class AdministrarLocalComponent {

}
