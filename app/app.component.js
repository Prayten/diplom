"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
Object.defineProperty(exports, "__esModule", { value: true });
const core_1 = require("@angular/core");
const colors_1 = require("./colors");
const date_fns_1 = require("date-fns");
const Subject_1 = require("rxjs/Subject");
let AppComponent = class AppComponent {
    constructor() {
        this.view = 'month';
        this.viewDate = new Date();
        this.refresh = new Subject_1.Subject();
        this.events = [
            {
                title: 'Click me',
                color: colors_1.colors.yellow,
                start: new Date(),
                draggable: true
            }, {
                title: 'Or click me',
                color: colors_1.colors.blue,
                start: new Date()
            }
        ];
    }
    addEvent() {
        this.events.push({
            title: 'New event',
            start: date_fns_1.startOfDay(new Date()),
            end: date_fns_1.endOfDay(new Date()),
            color: colors_1.colors.red,
            draggable: true,
            resizable: {
                beforeStart: true,
                afterEnd: true
            }
        });
        this.refresh.next();
    }
    eventClicked({ event }) {
        console.log('Event clicked', event);
    }
    ngOnInit() {
    }
};
AppComponent = __decorate([
    core_1.Component({
        moduleId: module.id,
        selector: 'my-app',
        templateUrl: 'app.component.html'
    })
], AppComponent);
exports.AppComponent = AppComponent;
//# sourceMappingURL=app.component.js.map