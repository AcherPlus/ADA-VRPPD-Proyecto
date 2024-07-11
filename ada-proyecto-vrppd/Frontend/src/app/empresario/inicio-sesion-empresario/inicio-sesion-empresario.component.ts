// inicio-sesion-empresario.component.ts
import { Component } from '@angular/core';
import {
  FormBuilder,
  FormGroup,
  ReactiveFormsModule,
  Validators,
} from '@angular/forms';
import { Router, RouterModule } from '@angular/router';
import { EmpresarioService } from '../../services/empresario.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-inicio-sesion-empresario',
  templateUrl: './inicio-sesion-empresario.component.html',
  styleUrls: ['./inicio-sesion-empresario.component.css'],
  imports: [RouterModule, ReactiveFormsModule, CommonModule],
  standalone: true,
})
export class InicioSesionEmpresarioComponent {
  loginForm: FormGroup;
  constructor(
    private fb: FormBuilder,
    private empresarioService: EmpresarioService,
    private router: Router
  ) {
    this.loginForm = this.fb.group({
      dni: ['', [Validators.required]],
      password: ['', [Validators.required]],
    });
  }

  onSubmit() {
    if (this.loginForm.valid) {
      const username = this.loginForm.get('dni')?.value;
      const password = this.loginForm.get('password')?.value;
      this.empresarioService.login(username, password).subscribe({
        next: (success) => {
          if (success) {
            this.empresarioService.setLoginStatus(true);
            this.router.navigate(['/inicio-empresario']);
          } else {
            alert('usuario o pass incorrecto');
          }
        },
        error: (error) => {
          alert('Error en el incio');
          console.error('Error', error);
        },
      });
    } else {
      console.log('Form is invalid');
    }
  }
}
