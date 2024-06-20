import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { PaginaInicioComponent } from "./pagina-inicio/pagina-inicio.component";
import { InicioSesionGeneralComponent } from "./inicio-sesion-general/inicio-sesion-general.component";
import {InicioSesionComponent} from "./proveedor/inicio-sesion/inicio-sesion.component";

@Component({
    selector: 'app-root',
    standalone: true,
    templateUrl: './app.component.html',
    styleUrl: './app.component.css',
    imports: [
      RouterOutlet, 
      PaginaInicioComponent, 
      InicioSesionGeneralComponent,
      InicioSesionComponent
    ]
})
export class AppComponent {
  title = 'ada-proyecto-vrppd';
}
