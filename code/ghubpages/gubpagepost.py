''' this builds github pages posts from a template. '''
import sys
import os
import datetime
from github import Github
from github import Auth

# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.gameitems.gamefunctions import credscheck


POST_FOLDER = "Z:/jackmanimationtest/_posts/"
POST_LOCATION = 'https://denisjackman.github.io/jackmanimationtest'
SECRET_FILE = 'Z:/pyproject/secrets/jackmanimation.json'
GITHUB_REPO = 'denisjackman/jackmanimationtest'


def create_post(cp_title,
                cp_date,
                cp_content='This is Test content.',
                cp_categories=None,
                cp_tags=None):
    '''Creates a post.'''
    cp_post = ''
    cp_cat_text = ''
    cp_tag_text = ''
    cp_post = '---\n'
    cp_post += 'layout: post\n'
    cp_post += f'title: "{cp_title}"\n'
    cp_post += f'date: {cp_date}\n'
    if cp_categories:
        cp_cat_text += 'categories: '
        for item in cp_categories:
            cp_cat_text += f'{item}, '
        cp_post += f'{cp_cat_text}\n'
    if cp_tags:
        cp_tag_text += 'tags: '
        for item in cp_tags:
            cp_tag_text += f'{item}, '
        cp_post += f'{cp_tag_text}\n'
    cp_post += '---\n\n'
    cp_post += f'{cp_content}'
    return cp_post


def open_github():
    '''Opens a connection to Github.'''
    og_credid = credscheck(SECRET_FILE)
    og_token = og_credid['jack_dev_key']
    og_auth = Auth.Token(og_token)
    og_github = Github(auth=og_auth)
    return og_github


def write_post(wp_post):
    '''Writes a post to a file.'''
    wp_file_name = f'{POST_FOLDER}{datetime.datetime.now().strftime("%Y-%m-%d")}-test-post.md'
    wp_target = f'_posts/{datetime.datetime.now().strftime("%Y-%m-%d")}-test-post.md'
    with open(wp_file_name, 'w', encoding='utf-8-sig') as wp_file:
        wp_file.write(wp_post)
    return wp_target


def main():
    '''Main function.'''
    print("[-] Starting post creation...")
    main_content = ''
    main_github = open_github()
    print("[+] Creating post...")
    for repo in main_github.get_user().get_repos():
        main_content += f"* [{repo.name}](https://github.com/{repo.owner.login}/{repo.name})\n"
    main_post = create_post("Test Post",
                            datetime.datetime.now().strftime("%Y-%m-%d"),
                            main_content)
    print("[+] Post created.")
    print("[+] Writing post...")
    main_file = write_post(main_post)
    print(f'[+] Post folder  : {POST_FOLDER}')
    print(f'[+] Post URL     : {POST_LOCATION}')
    print(f'[+] Post Content : {main_file}')
    main_github.close()
    print("[-] Finished.")


if __name__ == "__main__":
    main()
