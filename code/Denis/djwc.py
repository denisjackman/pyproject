''' djewc '''
import os
import shutil
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup

# Set up headers to mimic a browser request
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
}


def create_dir_structure(url):
    ''' Function to create directory structure to mirror the website '''
    # Parse the URL
    parsed_url = urlparse(url)
    path = parsed_url.path
    # Replace '/' with system's path separator to create local directories
    local_path = path.lstrip("/").replace("/", os.sep)
    if not local_path.endswith(('.html', '.htm')):
        local_path = os.path.join(local_path, "index.html")  # Default to index.html for non-file paths
    local_folder = os.path.dirname(local_path)
    # Create the directory structure
    if not os.path.exists(local_folder):
        print(f'[-] (local_folder){local_folder}')
        os.makedirs(local_folder)
    return local_path


def download_page(url):
    '''Function to download the content of a URL'''
    try:
        response = requests.get(url, headers=HEADERS, timeout=6)
        response.raise_for_status()
        local_path = create_dir_structure(url)
        # Write the HTML content to a local file
        with open(local_path, "wb") as file:
            file.write(response.content)
        return response.text
    except requests.RequestException as e:
        print(f"Failed to download {url}: {e}")
        return None


def download_asset(asset_url):
    '''# Function to download assets (CSS, images, JS files, etc.)'''
    try:
        response = requests.get(asset_url, headers=HEADERS, stream=True, timeout=6)
        response.raise_for_status()
        asset_path = create_dir_structure(asset_url)
        # Save the asset
        with open(asset_path, "wb") as file:
            shutil.copyfileobj(response.raw, file)
    except requests.RequestException as e:
        print(f"Failed to download asset {asset_url}: {e}")


def parse_and_download(url, base_url, visited):
    '''# Function to parse the page, find links and assets, and recursively download'''
    if url in visited:
        return
    visited.add(url)
    html_content = download_page(url)
    if not html_content:
        return
    soup = BeautifulSoup(html_content, "html.parser")
    # Recursively download linked pages
    for link in soup.find_all("a", href=True):
        next_url = urljoin(base_url, link["href"])
        # Only follow links within the same domain
        if urlparse(next_url).netloc == urlparse(base_url).netloc:
            parse_and_download(next_url, base_url, visited)
    # Download linked assets (CSS, JS, images)
    for asset in soup.find_all(["img", "script", "link"]):
        asset_url = None
        if asset.name == "img" and asset.get("src"):
            asset_url = urljoin(base_url, asset["src"])
        elif asset.name == "script" and asset.get("src"):
            asset_url = urljoin(base_url, asset["src"])
        elif asset.name == "link" and asset.get("href") and asset["rel"] == ["stylesheet"]:
            asset_url = urljoin(base_url, asset["href"])
        if asset_url:
            download_asset(asset_url)


def crawl_website(start_url):
    '''# Main function to start the process'''
    base_url = start_url
    visited = set()
    parse_and_download(start_url, base_url, visited)


if __name__ == "__main__":
    WEBSITE_URL = "https://beta.the-eye.eu/public/Books/rpg.rem.uz/Traveller/"
    # Replace with the target URL
    crawl_website(WEBSITE_URL)
