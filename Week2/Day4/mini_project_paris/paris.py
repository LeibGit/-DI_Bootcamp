from pyowm.owm import OWM
owm = OWM('e57d4cad9f8a3f0cc066f010748dbccf')
mgr = owm.weather_manager()

def weather_info():
    user_location = int(input("Enter the location id you wish to search: "))
    observation = mgr.weather_at_id(user_location)  # the observation object is a box containing a weather object
    weather = observation.weather
    return weather

if __name__=="__main__":
    sf = weather_info()
    print(f"{sf.detailed_status} is the weather status.")
    wi = sf.wind()
    print(f"{wi['speed']} meters per second")
    print(f"Sunrise Time: {sf.sunrise_time(timeformat='iso')}")
    print(f"Sunset Time: {sf.sunset_time(timeformat='iso')}")