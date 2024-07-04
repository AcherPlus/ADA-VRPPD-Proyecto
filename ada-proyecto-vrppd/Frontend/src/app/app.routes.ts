import { Routes } from '@angular/router';
import { InicioSesionGeneralComponent } from './inicio-sesion-general/inicio-sesion-general.component';
import { PaginaInicioComponent } from './pagina-inicio/pagina-inicio.component';
import { InicioSesionEmpresarioComponent } from './empresario/inicio-sesion-empresario/inicio-sesion-empresario.component';
import { CrearCuentaEmpresarioComponent } from './empresario/crear-cuenta-empresario/crear-cuenta-empresario.component';
import { PrincipalEmpresarioComponent } from './empresario/principal-empresario/principal-empresario.component';
import { EnvioInputEmpresarioComponent } from './empresario/envio-input-empresario/envio-input-empresario.component';
import { EnvioResumenEmpresarioComponent } from './empresario/envio-resumen-empresario/envio-resumen-empresario.component';
import { VerSeguimientoEmpresarioComponent } from './empresario/ver-seguimiento-empresario/ver-seguimiento-empresario.component';
import { InicioSesionProveedorComponent } from './proveedor/inicio-sesion-proveedor/inicio-sesion-proveedor.component';
import { CrearCuentaProveedorComponent } from './proveedor/crear-cuenta-proveedor/crear-cuenta-proveedor.component';
import { BienvenidoProveedorComponent } from './proveedor/bienvenido-proveedor/bienvenido-proveedor.component';
import { HistorialProveedorComponent } from './proveedor/historial-proveedor/historial-proveedor.component';
import { ListaTransporteProveedorComponent } from './proveedor/lista-transporte-proveedor/lista-transporte-proveedor.component';
import { AlmacenesProveedorComponent } from './proveedor/almacenes-proveedor/almacenes-proveedor.component';
import { AsignarTransporteProveedorComponent } from './proveedor/asignar-transporte-proveedor/asignar-transporte-proveedor.component';
import { EditarAlmacenesProveedorComponent } from './proveedor/editar-almacenes-proveedor/editar-almacenes-proveedor.component';
import { EditarListaTransporteProveedorComponent } from './proveedor/editar-lista-transporte-proveedor/editar-lista-transporte-proveedor.component';
import { EditarProductosProveedorComponent } from './proveedor/editar-productos-proveedor/editar-productos-proveedor.component';
import { ProductosProveedorComponent } from './proveedor/productos-proveedor/productos-proveedor.component';

export const routes: Routes = [
    {path: 'pagina-inicio', component: PaginaInicioComponent},
    {path: 'iniciar-sesion-como', component: InicioSesionGeneralComponent},
    {path: 'empresario-sesion', component: InicioSesionEmpresarioComponent},
    {path: 'empresario-crear-cuenta', component: CrearCuentaEmpresarioComponent},
    {path: 'inicio-empresario', component: PrincipalEmpresarioComponent},
    {path: 'enviar-paquete', component: EnvioInputEmpresarioComponent},
    {path: 'resumen-envio', component: EnvioResumenEmpresarioComponent},
    {path: 'ver-seguimiento', component: VerSeguimientoEmpresarioComponent},
        // Proveedor
    { path: 'proveedor-sesion', component: InicioSesionProveedorComponent },
    { path: 'bienvenido-proveedor', component: BienvenidoProveedorComponent },
    { path: 'proveedor-crear-cuenta', component: CrearCuentaProveedorComponent },
    { path: 'historial-proveedor', component: HistorialProveedorComponent },
    { path: 'lista-transporte-proveedor', component: ListaTransporteProveedorComponent },
    { path: 'almacenes-proveedor', component: AlmacenesProveedorComponent },
    { path: 'asignar-transporte-proveedor', component: AsignarTransporteProveedorComponent },
    { path: 'editar-almacenes-proveedor', component: EditarAlmacenesProveedorComponent },
    { path: 'editar-lista-transporte-proveedor', component: EditarListaTransporteProveedorComponent },
    { path: 'editar-productos-proveedor', component: EditarProductosProveedorComponent },
    { path: 'productos-proveedor', component: ProductosProveedorComponent },

    { path: '**', redirectTo: '/pagina-inicio', pathMatch: 'full' },
];
