from __future__ import annotations
from datetime import datetime
from abc import ABC, abstractmethod


class Event:
    pass


class Scheduler:
    def __init__(self):
        self.calendar = self._create_calendar()

    def schedule(self, event: Event):
        today = datetime.today()
        self.calendar.add_event(event, today)

    def _create_calendar(self):
        return GregorianCalendar()


class ArabianScheduler(Scheduler):
    def _create_calendar(self):
        return ArabianCalendar()


class Calendar(ABC):
    def add_event(self, event: Event, date: datetime):
        pass


class GregorianCalendar(Calendar):
    def add_event(self, event: Event, date: datetime):
        print("Adding an event on the given date")


class ArabianCalendar(Calendar):
    def add_event(self, event: Event, date: datetime):
        print("Adding an event to the Arabian calendar")


def main():
    scheduler = Scheduler()
    scheduler.schedule(Event())

    a_scheduler = ArabianScheduler()
    a_scheduler.schedule(Event())


if __name__ == '__main__':
    main()
