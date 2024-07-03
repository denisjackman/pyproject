''' github access example '''
import sys
import os
from github import Github
from github import Auth

# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.gameitems.gamefunctions import credscheck  # noqa: E402


gh_credid = credscheck('Z:/pyproject/secrets/jackmanimation.json')
GH_TOKEN = gh_credid['alt_jack_dev_key']
gh_auth = Auth.Token(GH_TOKEN)
gh_github = Github(auth=gh_auth)

for repo in gh_github.get_user().get_repos():
    print(repo.name)

gh_github.close()
