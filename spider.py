import requests
import re
import urllib.parse as urlparse

target_url = input("Enter the URL : ")
target_links = set()
max_depth = 3  # Set a depth limit for crawling

def extract_links_from(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    try:
        response = requests.get(url, headers=headers)
        return re.findall('(?:href=")(.*?)"', response.content.decode(errors="ignore"))
    except requests.RequestException as e:
        print(f"Error during requests to {url} : {str(e)}")
        return []

def crawl(url, depth):
    if depth > max_depth:
        return
    href_links = extract_links_from(url)
    for link in href_links:
        link = urlparse.urljoin(url, link)

        if "#" in link:
            link = link.split("#")[0]

        if target_url in link and link not in target_links:
            target_links.add(link)
            print(link)
            crawl(link, depth + 1)

# Start the crawl
crawl(target_url, 0)