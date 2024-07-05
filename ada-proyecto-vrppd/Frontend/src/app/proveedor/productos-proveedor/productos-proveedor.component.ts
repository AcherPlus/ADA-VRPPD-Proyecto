import { Component, OnInit } from '@angular/core';
import { RouterModule } from '@angular/router';
import { NavbarBipComponent } from '../../navbar-bip/navbar-bip.component';
import { ProductoService } from '../../services/producto.service';
@Component({
  selector: 'app-productos-proveedor',
  standalone: true,
  imports: [RouterModule, NavbarBipComponent],
  templateUrl: './productos-proveedor.component.html',
  styleUrl: './productos-proveedor.component.css'
})
export class ProductosProveedorComponent implements OnInit{

  dataProductos: any[] = [];

  constructor(private productoService: ProductoService) { }

  ngOnInit(): void {
    this.getProductos();
  }

  getProductos(){
    this.productoService.getProductos().subscribe(data => {
      this.dataProductos = data;
    });

    console.log(this.dataProductos);
  }
}
