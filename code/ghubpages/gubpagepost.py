''' this builds github pages posts from a template. '''
import sys
import os
import datetime
from github import Github
from github import Auth

# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.gameitems.gamefunctions import credscheck  # noqa: E402


POST_FOLDER = "Z:/jackmanimationtest/_posts/"
POST_LOCATION = 'https://denisjackman.github.io/jackmanimationtest'
SECRET_FILE = 'Z:/pyproject/secrets/jackmanimation.json'


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
    og_token = og_credid['alt_jack_dev_key']
    og_auth = Auth.Token(og_token)
    og_github = Github(auth=og_auth)
    return og_github


def write_post(wp_post):
    '''Writes a post to a file.'''
    wp_file_name = f'{POST_FOLDER}{datetime.datetime.now().strftime("%Y-%m-%d")}-test-post.md'  # noqa E501
    with open(wp_file_name, 'w') as wp_file:
        wp_file.write(wp_post)


def main():
    '''Main function.'''
    print("[-] Starting post creation...")
    print("[+] Creating post...")
    main_post = create_post("Test Post", datetime.datetime.now().strftime("%Y-%m-%d")) # noqa E501
    print(f"[+] Post created.{main_post}")
    print("[+] Writing post...")
    write_post(main_post)
    print("[+] Post written.")
    print("[+] Post saved.")
    print("[+] Post published.")
    print("[+] Post complete.")
    print(f'[+] Post folder  : {POST_FOLDER}')
    print(f'[+] Post URL     : {POST_LOCATION}')
    print("[-] Finished.")


if __name__ == "__main__":
    main()
