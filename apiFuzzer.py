import requests
import sys

res = requests.get(url=f"https://catfact.ninja/fact")
print (res)
data = res.json()
print (data)