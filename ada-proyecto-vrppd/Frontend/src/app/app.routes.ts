import { Routes } from '@angular/router';
import { InicioSesionGeneralComponent } from './inicio-sesion-general/inicio-sesion-general.component';
import { PaginaInicioComponent } from './pagina-inicio/pagina-inicio.component';
import { InicioSesionEmpresarioComponent } from './empresario/inicio-sesion-empresario/inicio-sesion-empresario.component';
import { CrearCuentaEmpresarioComponent } from './empresario/crear-cuenta-empresario/crear-cuenta-empresario.component';
import { PrincipalEmpresarioComponent } from './empresario/principal-empresario/principal-empresario.component';
import { EnvioInputEmpresarioComponent } from './empresario/envio-input-empresario/envio-input-empresario.component';
import { EnvioResumenEmpresarioComponent } from './empresario/envio-resumen-empresario/envio-resumen-empresario.component';
import { VerSeguimientoEmpresarioComponent } from './empresario/ver-seguimiento-empresario/ver-seguimiento-empresario.component';

export const routes: Routes = [
    {path: 'pagina-inicio', component: PaginaInicioComponent},
    {path: 'iniciar-sesion-como', component: InicioSesionGeneralComponent},
    {path: 'empresario-sesion', component: InicioSesionEmpresarioComponent},
    {path: 'empresario-crear-cuenta', component: CrearCuentaEmpresarioComponent},
    {path: 'inicio-empresario', component: PrincipalEmpresarioComponent},
    {path: 'enviar-paquete', component: EnvioInputEmpresarioComponent},
    {path: 'resumen-envio', component: EnvioResumenEmpresarioComponent},
    {path: 'ver-seguimiento', component: VerSeguimientoEmpresarioComponent},
    {path: '**', redirectTo: '/pagina-inicio', pathMatch: 'full'}
];
