import { Component, OnInit } from '@angular/core';
import { NavbarBipComponent } from '../../navbar-bip/navbar-bip.component';
import { RouterModule } from '@angular/router';
import { MapaComponent } from "../mapa/mapa.component";

@Component({
  selector: 'app-administar-mapa',
  standalone: true,
  imports: [NavbarBipComponent, RouterModule, MapaComponent],
  templateUrl: './administar-mapa.component.html',
  styleUrl: './administar-mapa.component.css'
})
export class AdministarMapaComponent {


}
