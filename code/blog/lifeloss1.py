import requests
import time

# Configuration
site_url = "https://lifeloss.wordpress.com/wp-json/wp/v2/posts"
auth_url = "https://lifeloss.wordpress.com/wp-json/jwt-auth/v1/token"
username = "username"  # Replace with your WordPress username
password = "password"  # Replace with your WordPress password

# Get JWT Token
auth_payload = {
    "username": username,
    "password": password
}

auth_response = requests.post(auth_url, json=auth_payload)

if auth_response.status_code != 200:
    print(f"Authentication failed: {auth_response.status_code} - {auth_response.text}")
    exit()

token = auth_response.json().get("token")
print("Authenticated! Token received.")

# Set Authorization Header
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

# Fetch posts
params = {
    "per_page": 100,
    "page": 1,
    "orderby": "date",
    "order": "asc"
}

all_posts = []

while True:
    response = requests.get(site_url, headers=headers, params=params)

    if response.status_code != 200:
        print(f"Failed to fetch posts: {response.status_code}")
        break

    posts = response.json()

    if not posts:
        break

    all_posts.extend(posts)
    print(f"Fetched {len(posts)} posts from page {params['page']}")

    params["page"] += 1
    time.sleep(1)

# Print posts
for post in all_posts:
    print(f"Title: {post['title']['rendered']}")
    print(f"Date: {post['date']}")
    print(f"Link: {post['link']}\n")

print(f"Total posts retrieved: {len(all_posts)}")
