import requests

url = "https://www.google.com"  # Google is not setup to handle plain text
url1 = "https://icanhazdadjoke.com/"

#response  = requests.get(url, headers = {"Accept": "text/html"})
#response  = requests.get(url1, headers = {"Accept": "text/plain"}) # sends only the joke
response  = requests.get(url1, headers = {"Accept": "application/json"}) # sends a dict as a result in python



print(f"Your resposne to {url1} came back w/ status {response.status_code}")

print(response.text) # results in a string that looks like a dict but it is not one.
#print(response.json()) # results in a python dictionary

data = response.json()

print(data)

print(data['id'])

print(data['joke'])