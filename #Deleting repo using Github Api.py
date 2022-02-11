#Deleting repo using Github Api
import requests
import os
import json
from requests.api import head
username=input("Enter your githu Username:")
token=input("Enter token:")
reponame=input("Enter the Repo name:")
github_url="https://api.github.com/"
headers={"Authorization": "token {}".format(token)}
data={"name": "{}".format(reponame)}
r=requests.delete("https://api.github.com/repos/{}/{}".format(username,reponame),headers=headers)
print (r)