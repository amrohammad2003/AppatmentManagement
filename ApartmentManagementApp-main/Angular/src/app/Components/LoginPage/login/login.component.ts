import { Component, ChangeDetectorRef } from '@angular/core';
import { faHouse, faUser, faLock } from '@fortawesome/free-solid-svg-icons';
import { faGoogle, faFacebook } from '@fortawesome/free-brands-svg-icons';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-login',
  standalone: true,
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
  imports: [FontAwesomeModule, FormsModule] // ✅ Fix: Add missing modules
})
export class LoginComponent {
  faHouse = faHouse;
  faUser = faUser;
  faLock = faLock;
  faGoogle = faGoogle;
  faFacebook = faFacebook;

  username: string = '';
  password: string = '';

  constructor(private cdr: ChangeDetectorRef) {}

  ngOnInit() {
    this.cdr.detectChanges(); // ✅ Fix: Ensure FontAwesome icons load properly
  }

  onLogin() {
    console.log('Logging in with:', this.username, this.password);
    // TODO: Implement actual login logic
  }

  onGoogleLogin() {
    console.log('Logging in with Google');
    // TODO: Implement Google login
  }

  onFacebookLogin() {
    console.log('Logging in with Facebook');
    // TODO: Implement Facebook login
  }
}
