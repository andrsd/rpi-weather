# RPI-WEATHER

## Dependencies

- datetime
- urllib
- darkskylib - API for Dark Sky
- geoip2 - for getting locations from IP (optional)
- kivy

## Install

### Config file

* Use the `weather.config.sample` and create the `weather.config` file

### Get Dark Sky API Key

* Get the API key from [dark sky](https://darksky.net/dev/register)
* Place the key into `weather.config` under `[darksky]` section into `api_key` parameter

### Using GeoIP

* If you get `GeoLite2-City.mmdb` and place it in `data/`, then the code will try to look up
  your location (the name of your town) based on the geo location. If you do not want to do that,
  enter your `latitude` and `longitude` parameters under `[location]` section in `weather.config`.


## ACKNOWLEDGEMENTS

This product includes GeoLite2 data created by MaxMind, available from
<a href="https://www.maxmind.com">https://www.maxmind.com</a>.

Powered by <a href="https://darksky.net/poweredby/">Dark Sky</a>.
