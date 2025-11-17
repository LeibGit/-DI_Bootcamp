from pyowm.owm import OWM
owm = OWM('e57d4cad9f8a3f0cc066f010748dbccf')

mgr = owm.weather_manager()
mgr2 = owm.airpollution_manager()

def weather_info():
    user_location = input("Enter the location id you wish to search: ")
    observation = mgr.forecast_at_place(user_location, '3h').forecast  # the observation object is a box containing a weather object
    weathers = observation.weathers

    coi = mgr.coindex_around_coords(
        lat, lon, 
        start=start
    )

    results = []
    for weather in observation:
       results.append(weather.detailed_status)
    return results
    
if __name__=="__main__":
    print(weather_info())