import { Component, OnInit } from '@angular/core';
import { NavbarBipComponent } from "../../navbar-bip/navbar-bip.component";
import { RouterModule } from '@angular/router';
import { LocalService } from '../../services/local.service';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-administrar-local',
  standalone: true,
  imports: [NavbarBipComponent, RouterModule, FormsModule],
  templateUrl: './administrar-local.component.html',
  styleUrl: './administrar-local.component.css'
})
export class AdministrarLocalComponent implements OnInit {
  localesUbicaciones: any[] = [];
  tipoSeleccionado: string = '';
  localesFiltrados: any[] = [];

    constructor(private localService:LocalService){}

    ngOnInit(){
        this.obtenerLocales();
    }
    
    obtenerLocales() {
      this.localService.getLocales().subscribe(dataLocal => {
        this.localesUbicaciones = dataLocal;
      });
    }

}
