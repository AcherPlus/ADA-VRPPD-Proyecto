import { Component, OnInit } from '@angular/core';
import { NavbarBipComponent } from '../../navbar-bip/navbar-bip.component';
import { RouterModule } from '@angular/router';
import { EmpresarioService } from '../../services/empresario.service';

@Component({
  selector: 'app-principal-empresario',
  standalone: true,
  templateUrl: './principal-empresario.component.html',
  styleUrl: './principal-empresario.component.css',
  imports: [NavbarBipComponent, RouterModule],
})
export class PrincipalEmpresarioComponent implements OnInit {
  nombreCompleto: string;

  constructor(private empresarioService: EmpresarioService) {
    this.nombreCompleto = '';
  }

  ngOnInit(): void {
    const empresario = this.empresarioService.getEmpresarioLogueado();
    this.nombreCompleto = empresario ? empresario.nombres : 'Empresario';
  }
}
