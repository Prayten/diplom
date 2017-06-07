import {NgModule} from '@angular/core';
import {BrowserModule} from '@angular/platform-browser';
import {FormsModule} from '@angular/forms';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {CalendarModule} from 'angular-calendar';
import {HttpModule} from "@angular/http";

import {CalendarService} from './calendar.service';
import {AppComponent} from './app.component';

@NgModule({
    imports: [
        BrowserModule,
        FormsModule,
        HttpModule,
        BrowserAnimationsModule,
        CalendarModule.forRoot()
    ],
    declarations: [AppComponent],
    providers: [CalendarService],
    bootstrap: [AppComponent]
})
export class AppModule {
}