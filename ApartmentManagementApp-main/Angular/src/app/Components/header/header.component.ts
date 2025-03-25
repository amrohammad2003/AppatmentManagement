import { Component } from '@angular/core';
import { RouterModule } from '@angular/router'; // ✅ Import RouterModule

@Component({
  selector: 'app-header',
  standalone: true,
  imports: [RouterModule], // ✅ Add RouterModule

  templateUrl: './header.component.html',
  styleUrl: './header.component.css'
})
export class HeaderComponent {

}
