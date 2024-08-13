''' github access example '''
import sys
import os
from github import Github
from github import Auth


# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.gameitems.gamefunctions import credscheck


gh_credid = credscheck('Z:/pyproject/secrets/jackmanimation.json')
GH_TOKEN = gh_credid['jack_dev_key']
gh_auth = Auth.Token(GH_TOKEN)
gh_github = Github(auth=gh_auth)

for repo in gh_github.get_user().get_repos():
    print(f"* [{repo.name}](https://github.com/{repo.owner.login}/{repo.name})")

gh_github.close()
