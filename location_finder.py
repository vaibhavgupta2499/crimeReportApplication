'''location_finder.py'''

from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geoapiExercises")

def loc_find(lat,long):
    location = geolocator.geocode(str(lat)+","+str(long))
    return(location)