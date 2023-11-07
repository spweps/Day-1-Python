import requests
from bs4 import BeautifulSoup

# The URL of the webpage you want to scrape
url = 'https://dalessuperstore.com/c-1210724-shop-by-auto-part-category-gas-vehicle-emissions-catalytic-converters.html'

def scrape_page(url):
    sku_list = []  # Create a list to store the scraped SKUs

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the specific HTML elements containing SKUs
        sku_elements = soup.find_all('div', class_='sku')  # Update with the actual element class
        
        for sku_element in sku_elements:
            sku = sku_element.text.strip()
            sku_list.append(sku)  # Add the scraped SKU to the list

    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

    return sku_list  # Return the list of scraped SKUs

scraped_skus = scrape_page(url)

# Print the list of scraped SKUs
for sku in scraped_skus:
    print(f"SKU: {sku}")
