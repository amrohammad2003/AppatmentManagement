import { bootstrapApplication } from '@angular/platform-browser';
import { provideRouter } from '@angular/router';
import { provideHttpClient } from '@angular/common/http';
import { routes } from './app/app.routes';
import { AppComponent } from './app/app.component';
import { ApiService } from './app/Services/api.service'; 
import { importProvidersFrom } from '@angular/core';
import { CommonModule } from '@angular/common';  // ✅ FIX: Import CommonModule

bootstrapApplication(AppComponent, {
  providers: [
    provideRouter(routes),
    provideHttpClient(),
    importProvidersFrom(CommonModule),  // ✅ FIX: Add CommonModule
    ApiService 
  ]
});
