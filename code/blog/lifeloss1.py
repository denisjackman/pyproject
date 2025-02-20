''' This script fetches all ll1_posts from a WordPress site using the WordPress REST API.
    It requires the requests library to be installed. '''
import time
import sys
import requests


# Configuration
SITE_URL = "https://lifeloss.wordpress.com/wp-json/wp/v2/ll1_posts"
AUTH_URL = "https://lifeloss.wordpress.com/wp-json/jwt-auth/v1/token"
USERNAME = "USERNAME"  # Replace with your WordPress USERNAME
PASSWORD = "PASSWORD"  # Replace with your WordPress PASSWORD

# Get JWT Token
auth_payload = {
    "USERNAME": USERNAME,
    "PASSWORD": PASSWORD
}

auth_ll1_response = requests.post(AUTH_URL, json=auth_payload, timeout=10)

if auth_ll1_response.status_code != 200:
    print(f"Authentication failed: {auth_ll1_response.status_code} - {auth_ll1_response.text}")
    sys.exit()

token = auth_ll1_response.json().get("token")
print("Authenticated! Token received.")

# Set Authorization Header
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

# Fetch ll1_posts
params = {
    "per_page": 100,
    "page": 1,
    "orderby": "date",
    "order": "asc"
}

all_ll1_posts = []

while True:
    ll1_response = requests.get(SITE_URL, headers=headers, params=params, timeout=10)

    if ll1_response.status_code != 200:
        print(f"Failed to fetch posts: {ll1_response.status_code}")
        break

    ll1_posts = ll1_response.json()

    if not ll1_posts:
        break

    all_ll1_posts.extend(ll1_posts)
    print(f"Fetched {len(ll1_posts)} ll1_posts from page {params['page']}")

    params["page"] += 1
    time.sleep(1)

# Print ll1_posts
for ll1_post in all_ll1_posts:
    print(f"Title: {ll1_post['title']['rendered']}")
    print(f"Date: {ll1_post['date']}")
    print(f"Link: {ll1_post['link']}\n")

print(f"Total posts retrieved: {len(all_ll1_posts)}")
