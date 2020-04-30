from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="specify_your_app_name_here")
location = geolocator.geocode("175 5th avenue NYC")
print(location.address)
print((location.latitude, location.longitude))