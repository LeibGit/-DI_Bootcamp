import requests
# part 1
giphy_api = "https://api.giphy.com/v1/gifs/search?q=hilarious&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My"

try:
    response = requests.get(giphy_api)
    print(response)
    response.raise_for_status()
except requests.status_codes != 202:
    print("error fetching api")

# part 2

user_input = input("Enter a phrase to return a relevant gif: ").lower().replace(' ', '').replace('.', '')
new_api_endpoint = f"https://api.giphy.com/v1/gifs/search?q={user_input}&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My"


response = requests.get(new_api_endpoint)
print(response)
response.raise_for_status()
if response.status_code != 200:
    print("No gifs found in this catagory, here are trending gifs of the day")
    print(requests.get("https://api.giphy.com/v1/gifs/trending&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My"))