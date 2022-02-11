from github import Github
import os
token=input("Enter the token:")
g=Github(token)
for repo in g.get_user().get_repos():
    print(repo.name)