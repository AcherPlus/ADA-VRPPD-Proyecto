import { Component, OnInit } from '@angular/core';
import { NavbarBipComponent } from '../../navbar-bip/navbar-bip.component';
import { RouterModule } from '@angular/router';
import { MapaComponent } from "../mapa/mapa.component";
import { LocalService } from "../../services/local.service";

@Component({
  selector: 'app-administar-mapa',
  standalone: true,
  imports: [NavbarBipComponent, RouterModule, MapaComponent],
  templateUrl: './administar-mapa.component.html',
  styleUrl: './administar-mapa.component.css'
})
export class AdministarMapaComponent implements OnInit{

  tipo: string = '';
  nombre: string = '';
  
  constructor(private localService:LocalService) { }

  ngOnInit() {}

  

  
}
