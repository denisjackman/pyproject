import requests
from bs4 import BeautifulSoup

# Define the blog URL
BLOG_URL = "https://ttmadness.blogspot.com/"

def get_blog_post_links(blog_url):
    ''' Extract all blog post URLs from a blogspot.com blog '''
    # Send an HTTP GET request
    response = requests.get(blog_url)
    if response.status_code != 200:
        print(f"Failed to retrieve the page, status code: {response.status_code}")
        return []

    # Parse the page content
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract all links from the page
    post_links = set()
    for link in soup.find_all("a", href=True):
        href = link["href"]
        if "blogspot.com" in href and href != blog_url:
            post_links.add(href)

    return sorted(post_links)

# Fetch and display blog post URLs
if __name__ == "__main__":
    urls = get_blog_post_links(BLOG_URL)
    if urls:
        print("Blog Post URLs:")
        for url in urls:
            print(url)
    else:
        print("No blog post links found.")
