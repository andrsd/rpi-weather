#!/usr/bin/env python

import os
import sys
import urllib
from darksky import forecast

from kivy.app import App
from kivy.config import Config
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.metrics import sp
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)

Config.read('weather.config')

class MainWidget(Widget):
    def __init__(self):
        super(MainWidget, self).__init__()

        self.get_location()
        self.weather = forecast(
            Config.get('darksky', 'api_key'),
            *self.location,
            units = Config.get('darksky', 'units'))
        self.update()

    def get_location(self):
        mmdb_file = Config.get('geolite2', 'db')
        if os.path.isfile(mmdb_file):
            # get my IP
            ip = urllib.request.urlopen('http://icanhazip.com/').read().decode("utf-8").strip()

            import geoip2.database
            reader = geoip2.database.Reader(mmdb_file)
            response = reader.city(ip)
            self.location = response.location.latitude, response.location.longitude
            self.name = response.city.name
            if response.subdivisions.most_specific.iso_code:
                self.name += ", " + response.subdivisions.most_specific.iso_code
            reader.close()
        else:
            self.location = Config.get('location', 'latitude'), Config.get('location', 'longitude')
            self.name = Config.getdefault('location', 'name', None)

    def refresh(self, dt):
        self.weather.refresh(
            units = Config.get('darksky', 'units')
        )
        self.update()

    def update(self):
        pass


class WeatherApp(App):
    def build(self):
        layout = Config.get("main", "layout")

        # load the .kv file for the layout
        Builder.load_file(layout + ".kv")
        # build the python object
        __import__(layout)
        module = sys.modules[layout]
        class_ = getattr(module, layout)
        main = class_()

        Clock.schedule_interval(main.refresh, int(Config.get('main', 'refresh')))
        return main

if __name__ == '__main__':
    WeatherApp().run()
