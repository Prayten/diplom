import {Injectable} from '@angular/core';
import {Http} from '@angular/http';
import {CalendarEvent} from 'angular-calendar';
import 'rxjs/add/operator/toPromise';

@Injectable()
export class CalendarService {

    private baseUrl = 'http://localhost:8000/event/';

    constructor(private http: Http) {
    }

    getEvents(): Promise<CalendarEvent[]> {
        let page = 1;
        return this.http.get(`${this.baseUrl}?page=${page}`)
            .toPromise()
            .then(response => response.json().results as CalendarEvent[])
            .catch(CalendarService.handleError);
    }

    private static handleError(error: any): Promise<any> {
        console.error('An error occurred', error); // for demo purposes only
        return Promise.reject(error.message || error);
    }
}