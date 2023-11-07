import requests
from bs4 import BeautifulSoup

# Replace with the URL of the webpage you want to start from
start_url = 'https://dalessuperstore.com/c-962415-shop-by-auto-part-category.html'

def scrape_page(url):
    duplicate_listings = set()  # Use a set to automatically handle duplicates

    headers = {
        'User-Agent': 'Your User Agent String Here'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Replace with the actual HTML element selectors
        sku_elements = soup.find_all('div', class_='product-model')
        link_elements = soup.find_all('a', class_='product-link')

        for sku_element, link_element in zip(sku_elements, link_elements):
            sku = sku_element.text.strip()
            listing = link_element.text.strip()
            duplicate_listings.add((sku, listing))

        # Find and follow links to child folders
        folder_links = soup.find_all('a', class_='category-name')

        for link in folder_links:
            child_url = link['href']
            if not child_url.startswith('http'):
                child_url = 'https://dalessuperstore.com' + child_url

            duplicate_listings.update(scrape_page(child_url))  # Use update for sets

    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

    return duplicate_listings

all_duplicate_listings = scrape_page(start_url)

# Print or process the list of duplicate listings
for sku, listing in all_duplicate_listings:
    print(f"SKU: {sku}, Listing: {listing}")
