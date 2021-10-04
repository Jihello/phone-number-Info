import geopy
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercises")
Latitude = "25.594095"
Longitude = "85.137566"
  
location = geolocator.reverse(Latitude+","+Longitude)
  
# Display
print(location)