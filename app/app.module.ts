import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { CalendarModule } from 'angular-calendar';

import { AppComponent } from './app.component';


@NgModule({
  imports: [ BrowserModule, FormsModule, CalendarModule.forRoot()  ],
  declarations: [ AppComponent ],
  providers: [  ],
  bootstrap: [ AppComponent ]
})

export class AppModule {

}
