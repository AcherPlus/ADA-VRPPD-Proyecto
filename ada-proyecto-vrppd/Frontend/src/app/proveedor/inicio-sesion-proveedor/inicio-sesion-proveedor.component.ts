import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-inicio-sesion-proveedor',
  standalone: true,
  imports: [],
  templateUrl: './inicio-sesion-proveedor.component.html',
  styleUrl: './inicio-sesion-proveedor.component.css'
})
export class InicioSesionProveedorComponent {
  loginForm: FormGroup;

  constructor(private fb: FormBuilder) {
    this.loginForm = this.fb.group({
      dni: ['', [Validators.required, Validators.pattern('\\d+')]],
      password: ['']
    });
  }

  onSubmit() {
    if (this.loginForm.valid) {
      const dni = this.loginForm.get('dni')?.value;
      const password = this.loginForm.get('password')?.value;
      console.log('DNI:', dni);
      console.log('Password:', password);
      // process and send to API
    } else {
      console.log('Form is invalid');
    }
  }

}
