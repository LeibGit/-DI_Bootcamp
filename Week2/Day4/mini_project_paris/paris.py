from pyowm.owm import OWM
owm = OWM('e57d4cad9f8a3f0cc066f010748dbccf')
mgr = owm.weather_manager()
observation = mgr.weather_at_place('Paris,FR')  # the observation object is a box containing a weather object
weather = observation.weather
weather.detailed_status

if __name__=="__main__":
    print(weather.detailed_status)