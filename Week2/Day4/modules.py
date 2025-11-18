import time
import requests

def time_to_load():
    start_time = time.time()
    response = requests.get("https://www.michellesparkling.com/")
    end_time = time.time()
    return f"It took roughly: {round(end_time - start_time)} seconds for this page to load." 
print(time_to_load())