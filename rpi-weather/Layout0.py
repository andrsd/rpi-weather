#!/usr/bin/env python

from main import MainWidget
from datetime import datetime, date, timedelta
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)

class Layout0(MainWidget):
    icon = ObjectProperty(None)
    current_temperature = ObjectProperty(None)
    today_lo_hi = ObjectProperty(None)

    hour1 = ObjectProperty(None)
    hour2 = ObjectProperty(None)
    hour3 = ObjectProperty(None)
    hour4 = ObjectProperty(None)
    temp_hour1 = ObjectProperty(None)
    temp_hour2 = ObjectProperty(None)
    temp_hour3 = ObjectProperty(None)
    temp_hour4 = ObjectProperty(None)

    day_name1 = ObjectProperty(None)
    day_name2 = ObjectProperty(None)
    day_name3 = ObjectProperty(None)
    day_name4 = ObjectProperty(None)
    day_lo_hi1 = ObjectProperty(None)
    day_lo_hi2 = ObjectProperty(None)
    day_lo_hi3 = ObjectProperty(None)
    day_lo_hi4 = ObjectProperty(None)

    def __init__(self):
        super(Layout0, self).__init__()

    def update(self):
        curr_source = self.icon.source
        filename = "icons/layout0/weather-{}.png".format(self.weather.currently.icon)
        if curr_source != filename:
            self.icon.source = filename
            self.icon.reload()

        self.current_temperature.text = "{}°".format(
            round(self.weather.currently.temperature)
        )
        self.today_lo_hi.text = "{} | [b]{}[/b]".format(
            round(self.weather.daily[0].temperatureMin),
            round(self.weather.daily[0].temperatureMax)
        )

        self.hour1.text = "{}".format(datetime.fromtimestamp(self.weather.hourly[1].time).strftime('%H'))
        self.hour2.text = "{}".format(datetime.fromtimestamp(self.weather.hourly[3].time).strftime('%H'))
        self.hour3.text = "{}".format(datetime.fromtimestamp(self.weather.hourly[5].time).strftime('%H'))
        self.hour4.text = "{}".format(datetime.fromtimestamp(self.weather.hourly[7].time).strftime('%H'))
        self.temp_hour1.text = "{}°".format(round(self.weather.hourly[1].temperature))
        self.temp_hour2.text = "{}°".format(round(self.weather.hourly[3].temperature))
        self.temp_hour3.text = "{}°".format(round(self.weather.hourly[5].temperature))
        self.temp_hour4.text = "{}°".format(round(self.weather.hourly[7].temperature))

        self.day_name1.text = "{}".format(datetime.fromtimestamp(self.weather.daily[1].time).strftime('%a')[0])
        self.day_name2.text = "{}".format(datetime.fromtimestamp(self.weather.daily[2].time).strftime('%a')[0])
        self.day_name3.text = "{}".format(datetime.fromtimestamp(self.weather.daily[3].time).strftime('%a')[0])
        self.day_name4.text = "{}".format(datetime.fromtimestamp(self.weather.daily[4].time).strftime('%a')[0])
        self.day_name5.text = "{}".format(datetime.fromtimestamp(self.weather.daily[5].time).strftime('%a')[0])

        self.day_lo_hi1.text = "{:2d} | [b]{:2d}[/b]".format(
            round(self.weather.daily[1].temperatureMin),
            round(self.weather.daily[1].temperatureMax)
        )
        self.day_lo_hi2.text = "{:2d} | [b]{:2d}[/b]".format(
            round(self.weather.daily[2].temperatureMin),
            round(self.weather.daily[2].temperatureMax)
        )
        self.day_lo_hi3.text = "{:2d} | [b]{:2d}[/b]".format(
            round(self.weather.daily[3].temperatureMin),
            round(self.weather.daily[3].temperatureMax)
        )
        self.day_lo_hi4.text = "{:2d} | [b]{:2d}[/b]".format(
            round(self.weather.daily[4].temperatureMin),
            round(self.weather.daily[4].temperatureMax)
        )
        self.day_lo_hi5.text = "{:2d} | [b]{:2d}[/b]".format(
            round(self.weather.daily[5].temperatureMin),
            round(self.weather.daily[5].temperatureMax)
        )
