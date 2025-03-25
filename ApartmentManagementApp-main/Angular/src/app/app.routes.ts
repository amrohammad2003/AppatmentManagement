import { Route } from '@angular/router';
import { UserListComponent } from './Components/Users/user-list/user-list.component';
import { HomePageComponent } from './Components/home-page/home-page.component';
import { ApartmentDetailsComponent } from './Components/apartment-details/apartment-details.component';
import { BuyHomesComponent } from './Components/buy-homes/buy-homes.component';
import { RentHomesComponent } from './Components/rent-homes/rent-homes.component';
import { LoginComponent } from './Components/LoginPage/login/login.component';

export const routes: Route[] = [
  { path: '', redirectTo: 'home-page', pathMatch: 'full' },  
  { path: 'home-page', component: HomePageComponent },
  { path: 'user-list', component: UserListComponent },

  // ✅ Dynamic Route to Fetch Apartment Details by ID
  { path: 'apartment/:id', component: ApartmentDetailsComponent },

  { path: 'buy-homes', component: BuyHomesComponent },
  { path: 'rent-homes', component: RentHomesComponent },
  { path: 'login', component: LoginComponent },
];
