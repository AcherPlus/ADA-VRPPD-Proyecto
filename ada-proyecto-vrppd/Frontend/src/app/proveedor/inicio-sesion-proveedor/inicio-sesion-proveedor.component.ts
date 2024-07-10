// inicio-sesion-proveedor.component.ts
import { Component } from '@angular/core';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { Router, RouterModule } from '@angular/router';
import { AuthService } from '../../services/auth.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-inicio-sesion-proveedor',
  templateUrl: './inicio-sesion-proveedor.component.html',
  styleUrls: ['./inicio-sesion-proveedor.component.css'],
  imports: [RouterModule, ReactiveFormsModule, CommonModule],
  standalone: true
})
export class InicioSesionProveedorComponent {
  loginForm: FormGroup;

  constructor(private fb: FormBuilder, private authService: AuthService, private router: Router) {
    this.loginForm = this.fb.group({
      dni: ['', [Validators.required, Validators.pattern('\\d+')]],
      password: ['', [Validators.required]]
    });
  }

  onSubmit() {
    if (this.loginForm.valid) {
      const dni = this.loginForm.get('dni')?.value;
      const password = this.loginForm.get('password')?.value;

      this.authService.login(dni, password).subscribe(
        success => {
          this.router.navigate(['/bienvenido-proveedor']);
        },
        error => {
          alert('Nombre de usuario o contraseña incorrectos');
          console.error('Error en el inicio de sesión', error);
        }
      );
    } else {
      console.log('Form is invalid');
    }
  }
}
