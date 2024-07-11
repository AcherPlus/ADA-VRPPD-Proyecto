import { Component, OnInit } from '@angular/core';
import { NavbarBipComponent } from "../../navbar-bip/navbar-bip.component";
import { RouterModule } from '@angular/router';
import { ProductoService } from '../../services/producto.service';


@Component({
    selector: 'app-envio-input-empresario',
    standalone: true,
    templateUrl: './envio-input-empresario.component.html',
    styleUrl: './envio-input-empresario.component.css',
    imports: [NavbarBipComponent, RouterModule]
})
export class EnvioInputEmpresarioComponent implements OnInit {
    productos: any[] = [];

    constructor(private productoService:ProductoService){}

    ngOnInit(){
        this.obtenerProductos();
    }

    obtenerProductos(){
        this.productoService.getProductos().subscribe(data => {
            this.productos = data;
            console.log(this.productos);
        })
    }
}
