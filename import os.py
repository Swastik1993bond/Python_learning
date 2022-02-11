import requests


url= "https://github.com/"

res= requests.get(url,timeout=5)
print(res.status_code)