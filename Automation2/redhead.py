import requests
from bs4 import BeautifulSoup

# Function to scrape core charges from a single listing page
def scrape_core_charge_listing(listing_url):
    response = requests.get(listing_url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    
    core_charge_element = soup.find('span', class_='core-charge')
    core_charge = core_charge_element.text.strip() if core_charge_element else None
    
    return core_charge

# Function to scrape core charges from a page of listings
def scrape_core_charges(url):
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    
    listing_data = []
    listing_links = soup.find_all('a', class_='listing-link')
    
    for link in listing_links:
        listing_url = link.get('href')
        part_number = link.find('span', class_='part-number').text.strip()
        core_charge = scrape_core_charge_listing(listing_url)
        
        if core_charge:
            listing_data.append((part_number, core_charge))
    
    return listing_data

# Main function to navigate through multiple pages
def main():
    base_url = "https://www.redheadsteeringgears.com/shop"
    total_pages = 17  # Adjust this based on the actual number of pages
    all_listing_data = []

    for page_number in range(1, total_pages + 1):
        page_url = base_url + str(page_number)
        listing_data = scrape_core_charges(page_url)
        
        all_listing_data.extend(listing_data)

    for part_number, core_charge in all_listing_data:
        print("Part Number:", part_number)
        print("Core Charge:", core_charge)
        print("=" * 30)

if __name__ == "__main__":
    main()
