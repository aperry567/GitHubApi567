import requests
import json


def github_id(username):
    """ retrieve a user's list of repositories, use this API """
    response = requests.get("https://api.github.com/users/"+username+"/repo")

    """ retrieve a user's output results in json format """
    resp_text = response.text
    resp_json = json.loads(resp_text)

    output = []
    for item in resp_json:
        output.append(resp_json.setdefault(item, output))
    return output


def github_repo(username, repo):
    """ retrieve a user's list of commits, use this API """
    response1 = requests.get("https://api.github.com/repos/"+username+"/"+repo+"/commits")

    repo_text = response1.text
    repo_json = json.loads(repo_text)
    return len(repo_json)


def main():
    """ main function"""
    username = input('Enter Your GitHub username:')
    print(username)

    github_id(username)

if __name__ == "__main__":
        main()