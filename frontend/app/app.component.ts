import {Component, OnInit, ChangeDetectionStrategy, EventEmitter} from '@angular/core';
import {Subject} from 'rxjs/Subject';
import {startOfDay, endOfDay} from 'date-fns';
import {CalendarEvent, CalendarEventTimesChangedEvent} from 'angular-calendar';
import {CalendarService} from './calendar.service';
import {colors} from './colors';

@Component({
    moduleId: module.id,
    selector: 'my-app',
    changeDetection: ChangeDetectionStrategy.OnPush,
    templateUrl: 'app.component.html'
})
export class AppComponent implements OnInit {

    view: string = 'day';

    viewDate1: Date;
    viewDate2: Date;
    viewDate3: Date;
    viewDate4: Date;
    viewDate5: Date;
    viewDate6: Date;

    viewDateChange: EventEmitter<Date> = new EventEmitter();

    // viewDate1: Date = new Date(2017, 5, 5);
    // viewDate2: Date = new Date(2017, 5, 6);
    // viewDate3: Date = new Date(2017, 5, 7);
    // viewDate4: Date = new Date(2017, 5, 8);
    // viewDate5: Date = new Date(2017, 5, 9);
    // viewDate6: Date = new Date(2017, 5, 10);

    refresh1: Subject<any> = new Subject();

    events: CalendarEvent[] = [{
        start: new Date(2017, 5, 8, 12, 0, 0),
        title: "Hello World!",
        color: colors.yellow,
        draggable: true,
        resizable: true
    }, {
        start: new Date(2017, 5, 6, 12, 0, 0),
        title: "Hello World!",
        color: colors.yellow,
        draggable: true,
        resizable: true
    }];

    constructor(private calendarService: CalendarService) {
        let today = new Date();
        today.setHours(0, 0, 0, 0);
        let shift = today.getDate() - today.getDay();
        this.viewDate1 = new Date(today.setDate(shift + 1));
        this.viewDate2 = new Date(today.setDate(shift + 2));
        this.viewDate3 = new Date(today.setDate(shift + 3));
        this.viewDate4 = new Date(today.setDate(shift + 4));
        this.viewDate5 = new Date(today.setDate(shift + 5));
        this.viewDate6 = new Date(today.setDate(shift + 6));
    }

    getEvents(): void {
        let self = this;
        this.calendarService
            .getEvents()
            .then(events => {
                // self.events = new Array<CalendarEvent>();
                // self.events = [];
                for (let i = 0; i < events.length; i++) {
                    self.events.push({
                        title: events[i].title,
                        start: new Date(events[i].start),
                        // end: new Date(events[i].end),
                        color: colors.blue
                        // draggable: true,
                        // resizable: true
                    });
                    // self.refresh1.next();
                }
                return events;
            })
            .then(() => self.refresh1.next());
    }

    previous(): void {
        let shift = - 7;
        this.viewDate1.setHours(24 * shift);
        this.viewDate2.setHours(24 * shift);
        this.viewDate3.setHours(24 * shift);
        this.viewDate4.setHours(24 * shift);
        this.viewDate5.setHours(24 * shift);
        this.viewDate6.setHours(24 * shift);
        this.refresh1.next();
    }

    next(): void {
        let shift = 7;
        this.viewDate1.setHours(24 * shift);
        this.viewDate2.setHours(24 * shift);
        this.viewDate3.setHours(24 * shift);
        this.viewDate4.setHours(24 * shift);
        this.viewDate5.setHours(24 * shift);
        this.viewDate6.setHours(24 * shift);
        this.refresh1.next();
    }

    refresh(): void {
        //     this.events.push({
        //         title: 'New event',
        //         color: colors.red,
        //         start: new Date(2017, 6, 7, 0, 0),
        //         draggable: true,
        //         resizable: {
        //             beforeStart: true,
        //             afterEnd: true
        //         }
        //     });
        // console.log('add event');
        this.refresh1.next();
    }

    // static eventClicked({event}: { event: CalendarEvent }): void {
    //     console.log('Event clicked', event);
    // }

    ngOnInit() {
        this.getEvents();
    }

    eventTimesChanged({event, newStart, newEnd}: CalendarEventTimesChangedEvent): void {
        event.start = newStart;
        event.end = newEnd;
        this.refresh1.next();
    }
}
