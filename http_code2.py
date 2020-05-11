import requests

url1 = "https://icanhazdadjoke.com/search"

response  = requests.get(url1, 
        headers = {"Accept": "application/json"},
        params = {"term": "cat", "limit": 2}) 


data = response.json()

print(data["results"])
