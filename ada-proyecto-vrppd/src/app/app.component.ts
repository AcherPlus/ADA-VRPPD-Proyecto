import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { PaginaInicioComponent } from "./pagina-inicio/pagina-inicio.component";

@Component({
    selector: 'app-root',
    standalone: true,
    templateUrl: './app.component.html',
    styleUrl: './app.component.css',
    imports: [RouterOutlet, PaginaInicioComponent]
})
export class AppComponent {
  title = 'ada-proyecto-vrppd';
}
