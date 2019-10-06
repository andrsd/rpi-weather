#!/usr/bin/env python
# -*- coding: utf-8 -*-

from main import MainWidget
from datetime import datetime, date, timedelta
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)

class Layout2(MainWidget):
    def __init__(self):
        super(Layout2, self).__init__()

    def update(self):
        self.current_temperature.text = "{}°".format(int(round(self.weather.currently.temperature)))
        self.day_lo_hi.text = "{}° / [b]{}°[/b]".format(
            int(round(self.weather.daily[0].temperatureMin)),
            int(round(self.weather.daily[0].temperatureMax))
        )

        self.precip_chance.text = "{}%".format(int(round(self.weather.currently.precipProbability * 100.)))
        wind_dir_idx = int(((self.weather.currently.windBearing + 22.5) % 360) / 45)
        wind_dir = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
        self.wind.text = "{} [b]{}[/b]".format(
            wind_dir[wind_dir_idx],
            int(round(self.weather.currently.windSpeed))
        )

        self.day1_name.text = "{}".format(datetime.fromtimestamp(self.weather.daily[1].time).strftime('%a')).upper()
        filename = "icons/layout2/weather-{}.png".format(self.weather.daily[1].icon)
        self.day1_icon.source = filename
        self.day1_icon.reload()
        self.day1_lo.text = "{:2d}°".format(int(round(self.weather.daily[1].temperatureMin)))
        self.day1_hi.text = "{:2d}°".format(int(round(self.weather.daily[1].temperatureMax)))
        self.day1_precip.text = "{}%".format(int(round(self.weather.daily[1].precipProbability * 100.)))
        self.day1_wind.text = "{}".format(int(round(self.weather.daily[1].windSpeed)))

        self.day2_name.text = "{}".format(datetime.fromtimestamp(self.weather.daily[2].time).strftime('%a')).upper()
        filename = "icons/layout2/weather-{}.png".format(self.weather.daily[2].icon)
        self.day2_icon.source = filename
        self.day2_icon.reload()
        self.day2_lo.text = "{:2d}°".format(int(round(self.weather.daily[2].temperatureMin)))
        self.day2_hi.text = "{:2d}°".format(int(round(self.weather.daily[2].temperatureMax)))
        self.day2_precip.text = "{}%".format(int(round(self.weather.daily[2].precipProbability * 100.)))
        self.day2_wind.text = "{}".format(int(round(self.weather.daily[2].windSpeed)))

        self.day3_name.text = "{}".format(datetime.fromtimestamp(self.weather.daily[3].time).strftime('%a')).upper()
        filename = "icons/layout2/weather-{}.png".format(self.weather.daily[3].icon)
        self.day3_icon.source = filename
        self.day3_icon.reload()
        self.day3_lo.text = "{:2d}°".format(int(round(self.weather.daily[3].temperatureMin)))
        self.day3_hi.text = "{:2d}°".format(int(round(self.weather.daily[3].temperatureMax)))
        self.day3_precip.text = "{}%".format(int(round(self.weather.daily[3].precipProbability * 100.)))
        self.day3_wind.text = "{}".format(int(round(self.weather.daily[3].windSpeed)))
