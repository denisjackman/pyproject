''' Extract all the blogs from a website '''

import requests
import time


def main():
    # WordPress API URL
    site_url = "https://lifeloss.wordpress.com/wp-json/wp/v2/posts"
    # site_url = "https://lifeloss.wordpress.com/""
    params = {"per_page": 100,  # Fetch up to 100 posts per request
              "page": 1,        # Start from page 1
              "orderby": "date",
              "order": "asc",   # Oldest posts first
              }
    all_posts = []

    while True:
        response = requests.get(site_url, params=params)

        if response.status_code != 200:
            print(f"Failed to fetch data: {response.status_code}")
            break

        posts = response.json()

        if not posts:
            break  # No more posts to fetch

        all_posts.extend(posts)
        print(f"Fetched {len(posts)} posts from page {params['page']}")

        params["page"] += 1  # Move to the next page
        time.sleep(1)  # Prevent rate limiting

    # Print posts
    for post in all_posts:
        print(f"Title: {post['title']['rendered']}")
        print(f"Date: {post['date']}")
        print(f"Link: {post['link']}\n")

    print(f"Total posts retrieved: {len(all_posts)}")


if __name__ == '__main__':
    main()
