import { Component, OnInit, ChangeDetectionStrategy } from '@angular/core';
import { colors } from './colors';
import { CalendarEvent, CalendarEventTimesChangedEvent } from 'angular-calendar';
import { startOfDay, endOfDay } from 'date-fns';
import { Subject } from 'rxjs/Subject';



@Component({
    moduleId: module.id,
    selector: 'my-app',
    changeDetection: ChangeDetectionStrategy.OnPush,
    templateUrl: 'app.component.html'
})

export class AppComponent implements OnInit{
    
    
    
    view: string = 'month';

    viewDate: Date = new Date();

    refresh: Subject<any> = new Subject();

    events: CalendarEvent[] = [
        {

            title: 'Click me',
            color: colors.yellow,
            start: new Date(),
            draggable: true
        }, {
            title: 'Or click me',
            color: colors.blue,
            start: new Date()
        }
    ];

    addEvent(): void{
        this.events.push({
            title: 'New event',
            start: startOfDay(new Date()),
            end: endOfDay(new Date()),
            color: colors.red,
            draggable: true,
            resizable: {
                beforeStart: true,
                afterEnd: true
            }

        });
        this.refresh.next();
    }
    
    eventClicked({event}: {event: CalendarEvent}): void{
        console.log('Event clicked', event);
    }
  
    ngOnInit(){
    
    }

    eventTimesChanged({event, newStart, newEnd}: CalendarEventTimesChangedEvent): void {
    event.start = newStart;
    event.end = newEnd;
    this.refresh.next();
  }
    
}
