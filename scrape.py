import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def fetch_text_from_url(url, visited, accumulated_text):
    """ Fetch and return the textual content of a webpage given its URL. """
    if url in visited:
        return accumulated_text
    print(f"Fetching {url}")
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        visited.add(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        accumulated_text.append(soup.get_text())  # Append current page text to the list
        
        for link in soup.find_all('a', href=True):
            absolute_link = urljoin(url, link['href'])
            if absolute_link not in visited and urlparse(absolute_link).netloc == urlparse(url).netloc:
                fetch_text_from_url(absolute_link, visited, accumulated_text)
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
    return accumulated_text

def main():
    start_url = "https://croquetdev.com/"
    visited_urls = set()
    all_texts = []
    fetch_text_from_url(start_url, visited_urls, all_texts)
    
    # Combine all text into one string
    combined_text = "\n".join(all_texts)
    
    # Write all text to a file
    with open("oxfordcroquet.txt", "w", encoding="utf-8") as file:
        file.write(combined_text)

    print("Text from all pages has been saved to croquet.txt.")

if __name__ == "__main__":
    main()
