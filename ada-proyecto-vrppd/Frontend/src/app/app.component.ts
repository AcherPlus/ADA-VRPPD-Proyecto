import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { InicioSesionComponent } from './empresario/inicio-sesion/inicio-sesion.component';
import { PaginaInicioComponent } from './pagina-inicio/pagina-inicio.component';
import { InicioSesionGeneralComponent } from './inicio-sesion-general/inicio-sesion-general.component';
import { InicioSesionProveedorComponent } from './proveedor/inicio-sesion-proveedor/inicio-sesion-proveedor.component';
import { CrearCuentaProveedorComponent } from './proveedor/crear-cuenta-proveedor/crear-cuenta-proveedor.component';
import {BienvenidoProveedorComponent} from './proveedor/bienvenido-proveedor/bienvenido-proveedor.component';
@Component({
  selector: 'app-root',
  standalone: true,
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
  imports: [
    //Importar lo necesario para que funcione la aplicacion
    RouterOutlet,
    FormsModule,
    ReactiveFormsModule,
    //Modulos de empresario
    InicioSesionComponent,

    //Modulos generales
    PaginaInicioComponent,
    InicioSesionGeneralComponent,

    //Modulos de proveedor
    InicioSesionProveedorComponent,
    CrearCuentaProveedorComponent,
    BienvenidoProveedorComponent
  ],
})
export class AppComponent {
  title = 'ada-proyecto-vrppd';
}
