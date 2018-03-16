""" Homework#4: """

import requests
import json


def github_id(username):
    """ retrieve a user's list of repositories, use this API """
    response = requests.get("https://api.github.com/users/"+username+"/repo")

    resp_text = response.text
    resp_json = json.loads(resp_text)
    
    total_commits = 0

    for item in resp_json:
        total_commits = len(item)
        print("GitHub user:",username, "Number of commits:",total_commits)
        

def github_repo(username, repo):
    response1 = requests.get("https://api.github.com/repos/"+username+"/"+repo+"/commits")

    repo_text = response1.text
    repo_json = json.loads(repo_text)
    #print("GitHub repo:", repo_json)
    return repo_json, len(repo_json)


def main():
    """ main function"""
    user_id = input('Enter Your GitHub username:')

    github_id(user_id)

if __name__ == "__main__":
        main()