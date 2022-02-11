#listing all the repos under github
import requests
import os
import json
github_url="https://api.github.com/"
data = {"type":"all","sort":"full_name","direction":"asc"}
unsername=input("Please us eyour Github Username:")
token=input("Enter token:")
headers={"Authorization": "token {}".format(token)}
output=requests.get(github_url+"user/repos"+"",data=json.dumps(data), headers=headers)
output=json.loads(output.text)
for reponame in output:
    print(reponame['name'])