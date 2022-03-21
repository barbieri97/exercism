""" this module create a clock """
from datetime import time as t

class Clock:
    """ create a clock """
    def __init__(self, hour, minute):
        self.hour_1, self.minute = divmod(minute, 60)
        self.hour_2 = divmod(hour + self.hour_1, 24)
        self.clock = t(hour=self.hour_2[1], minute=self.minute)

    def __repr__(self):
        return f'Clock({self.clock.hour}, {self.clock.minute})'

    def __str__(self):
        return self.clock.isoformat(timespec='minutes')

    def __eq__(self, other):
        if str(self) == str(other):
            return True
        return False

    def __add__(self, minutes):
        hora_1, minuto = divmod(self.minute + minutes, 60)
        hora = divmod(hora_1 + self.hour_2[1], 24)
        self.clock = t(hour=hora[1], minute=minuto)
        return self.clock.isoformat(timespec='minutes')

    def __sub__(self, minutes):
        hora_1, minuto = divmod(self.minute - minutes, 60)
        hora = divmod(hora_1 + self.hour_2[1], 24)
        self.clock = t(hour=hora[1], minute=minuto)
        return self.clock.isoformat(timespec='minutes')
