import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
import { AuthService } from '../services/auth.service';

@Component({
  selector: 'app-navbar-bip',
  standalone: true,
  imports: [RouterModule],
  templateUrl: './navbar-bip.component.html',
  styleUrl: './navbar-bip.component.css'
})
export class NavbarBipComponent {
  constructor(private authService: AuthService) { }

  logout(): void {
    this.authService.logout();
  }
}
