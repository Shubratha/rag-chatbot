# src/data_ingestion/web_scraper.py

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def is_internal_link(link, base_url):
    return urlparse(link).netloc == '' or urlparse(link).netloc == urlparse(base_url).netloc

def scrape_website(base_url, visited=None, max_pages=50):
    if visited is None:
        visited = set()

    docs = []
    to_visit = [base_url]

    while to_visit and len(visited) < max_pages:
        url = to_visit.pop()
        if url in visited:
            continue

        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.content, "html.parser")
            visited.add(url)

            # Extract visible text
            page_text = soup.get_text(separator="\n", strip=True)
            docs.append({"url": url, "content": page_text})

            # Find and queue internal links
            for link_tag in soup.find_all("a", href=True):
                link = urljoin(url, link_tag["href"])
                if is_internal_link(link, base_url) and link not in visited:
                    to_visit.append(link)

        except Exception as e:
            print(f"Error visiting {url}: {e}")

    return docs