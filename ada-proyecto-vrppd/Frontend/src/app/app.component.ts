import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { PaginaInicioComponent } from './pagina-inicio/pagina-inicio.component';
import { InicioSesionGeneralComponent } from './inicio-sesion-general/inicio-sesion-general.component';
import { InicioSesionProveedorComponent } from './proveedor/inicio-sesion-proveedor/inicio-sesion-proveedor.component';
import { CrearCuentaProveedorComponent } from './proveedor/crear-cuenta-proveedor/crear-cuenta-proveedor.component';
import {BienvenidoProveedorComponent} from './proveedor/bienvenido-proveedor/bienvenido-proveedor.component';
import { InicioSesionEmpresarioComponent } from "./empresario/inicio-sesion-empresario/inicio-sesion-empresario.component";
import { CrearCuentaEmpresarioComponent } from "./empresario/crear-cuenta-empresario/crear-cuenta-empresario.component";
import { PrincipalEmpresarioComponent } from "./empresario/principal-empresario/principal-empresario.component";
import { EnvioInputEmpresarioComponent } from "./empresario/envio-input-empresario/envio-input-empresario.component";
import { EnvioResumenEmpresarioComponent } from "./empresario/envio-resumen-empresario/envio-resumen-empresario.component";
import { NavbarBipComponent } from "./navbar-bip/navbar-bip.component";
import { VerSeguimientoEmpresarioComponent } from "./empresario/ver-seguimiento-empresario/ver-seguimiento-empresario.component";
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
        //Modulos generales
        PaginaInicioComponent,
        InicioSesionGeneralComponent,
        //Modulos de proveedor
        InicioSesionProveedorComponent,
        CrearCuentaProveedorComponent,
        BienvenidoProveedorComponent,
        InicioSesionEmpresarioComponent,
        CrearCuentaEmpresarioComponent,
        PrincipalEmpresarioComponent,
        EnvioInputEmpresarioComponent,
        EnvioResumenEmpresarioComponent,
        NavbarBipComponent,
        VerSeguimientoEmpresarioComponent
    ]
})
export class AppComponent {
  title = 'ada-proyecto-vrppd';
}
