from darksky.api import DarkSky
from darksky.types import languages, units, weather


API_KEY = 'e2fea81b36c2588f1315c4ad2b721989'

darksky = DarkSky(API_KEY)

latitude = 54.4912
longitude = -89.2354
forecast = darksky.get_forecast(
    latitude, longitude,
    extend=False, 
    lang=languages.ENGLISH, 
    units=units.AUTO,
    exclude=[weather.MINUTELY, weather.ALERTS] 
)

print(forecast.currently.temperature)

forecast.latitude 
forecast.longitude 
forecast.timezone

forecast.currently 






