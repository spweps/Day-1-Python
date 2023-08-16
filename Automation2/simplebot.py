import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
base_url = "https://dalessuperstore.com/catalog.html"

def scrape_listing(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Extract data from the listing page
        title = soup.find("h1", class_="title-class").get_text().strip()
        price = soup.find("span", class_="price-class").get_text().strip()
        # ... and other data
        
        return {"title": title, "price": price}  # Return a dictionary with scraped data
    else:
        print(f"Failed to retrieve content from {url}")
        return None

def scrape_recursive(url, item_to_search):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Scrape the page or perform other tasks as needed
        
        listing_links = []  # Modify this to find individual listing links on the current page
        
        for listing_link in listing_links:
            listing_url = base_url + listing_link
            listing_data = scrape_listing(listing_url)
            if listing_data:
                if item_to_search in listing_data.values():
                    return True
        
        subcategory_links = []  # Modify this to find subcategory links on the current page
        
        for subcategory_link in subcategory_links:
            subcategory_url = base_url + subcategory_link
            if scrape_recursive(subcategory_url, item_to_search):
                return True

        category_links = []  # Modify this to find category links on the current page
        
        for category_link in category_links:
            category_url = base_url + category_link
            if scrape_recursive(category_url, item_to_search):
                return True
    
    return False

def main():
    item_to_search = input("Enter the Item# to search for: ")
    start_url = base_url  # Start with the main page
    item_exists = scrape_recursive(start_url, item_to_search)
    
    if item_exists:
        print(f"Item# {item_to_search} exists on the website.")
    else:
        print(f"Item# {item_to_search} does not exist on the website.")

if __name__ == "__main__":
    main()
