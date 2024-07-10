// app.module.ts
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';

import { AppComponent } from './app.component';
import { routes } from './app.routes';

// Importar los componentes
import { PaginaInicioComponent } from './pagina-inicio/pagina-inicio.component';
import { InicioSesionGeneralComponent } from './inicio-sesion-general/inicio-sesion-general.component';
import { InicioSesionProveedorComponent } from './proveedor/inicio-sesion-proveedor/inicio-sesion-proveedor.component';
import { BienvenidoProveedorComponent } from './proveedor/bienvenido-proveedor/bienvenido-proveedor.component';
import { InicioSesionEmpresarioComponent } from "./empresario/inicio-sesion-empresario/inicio-sesion-empresario.component";
import { CrearCuentaEmpresarioComponent } from "./empresario/crear-cuenta-empresario/crear-cuenta-empresario.component";
import { PrincipalEmpresarioComponent } from "./empresario/principal-empresario/principal-empresario.component";
import { EnvioInputEmpresarioComponent } from "./empresario/envio-input-empresario/envio-input-empresario.component";
import { EnvioResumenEmpresarioComponent } from "./empresario/envio-resumen-empresario/envio-resumen-empresario.component";
import { NavbarBipComponent } from "./navbar-bip/navbar-bip.component";
import { AsignarTransporteProveedorComponent } from './proveedor/asignar-transporte-proveedor/asignar-transporte-proveedor.component';
import { VerSeguimientoEmpresarioComponent } from "./empresario/ver-seguimiento-empresario/ver-seguimiento-empresario.component";
import { HistorialProveedorComponent } from './proveedor/historial-proveedor/historial-proveedor.component';
import { AlmacenesProveedorComponent } from './proveedor/almacenes-proveedor/almacenes-proveedor.component';
import { EditarAlmacenesProveedorComponent } from './proveedor/editar-almacenes-proveedor/editar-almacenes-proveedor.component';
import { ProductosProveedorComponent } from './proveedor/productos-proveedor/productos-proveedor.component';
import { EditarProductosProveedorComponent } from './proveedor/editar-productos-proveedor/editar-productos-proveedor.component';
import { ListaTransporteProveedorComponent } from './proveedor/lista-transporte-proveedor/lista-transporte-proveedor.component';
import { EditarListaTransporteProveedorComponent } from './proveedor/editar-lista-transporte-proveedor/editar-lista-transporte-proveedor.component';

import { AuthGuard } from './services/auth.guard';
import { AuthService } from './services/auth.service';
import { AuthInterceptor } from './services/auth.interceptor';

@NgModule({
  declarations: [
    AppComponent,
    PaginaInicioComponent,
    InicioSesionGeneralComponent,
    InicioSesionProveedorComponent,
    BienvenidoProveedorComponent,
    InicioSesionEmpresarioComponent,
    CrearCuentaEmpresarioComponent,
    PrincipalEmpresarioComponent,
    EnvioInputEmpresarioComponent,
    EnvioResumenEmpresarioComponent,
    VerSeguimientoEmpresarioComponent,
    HistorialProveedorComponent,
    AlmacenesProveedorComponent,
    EditarAlmacenesProveedorComponent,
    ProductosProveedorComponent,
    EditarProductosProveedorComponent,
    ListaTransporteProveedorComponent,
    EditarListaTransporteProveedorComponent,
    NavbarBipComponent,
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    RouterModule.forRoot(routes)
  ],
  providers: [
    AuthService,
    AuthGuard,
    {
      provide: HTTP_INTERCEPTORS,
      useClass: AuthInterceptor,
      multi: true
    }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
