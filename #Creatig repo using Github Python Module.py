#Creatig repo using Github Python Module:
import requests
import os
import json
from requests.api import head
token=input("Enter token:")
reponame=input("Enter the Repo name:")
github_url="https://api.github.com/"
headers={"Authorization": "token {}".format(token)}
data={"name": "{}".format(reponame)}
r=requests.post(github_url+"user/repos"+"",data=json.dumps(data), headers=headers)
print (r)