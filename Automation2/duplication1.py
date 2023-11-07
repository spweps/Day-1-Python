import requests
from bs4 import BeautifulSoup

# Base URL of your website
base_url = "https://dalessuperstore.com/"
# Initial URL of the most general category page
start_category_url = base_url + "/c-962415-shop-by-part-category.html"

def get_listings_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        listings_data = []

        # Extract SKU and URL for each listing
        listings = soup.find_all("div", class_="listing")
        for listing in listings:
            sku = listing.find("span", class_="sku").text.strip()
            listing_url = base_url + listing.find("a", href=True)["href"]

            listings_data.append({"sku": sku, "url": listing_url})

        return listings_data
    else:
        print("Failed to retrieve listings data")
        return []

def extract_cross_reference(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        cross_reference = soup.find("span", class_="cross-reference").text.strip()
        return cross_reference
    else:
        return None

def find_duplicate_listings(listings_data):
    # ... (same as before)

def navigate_listings(category_url):
    page_number = 1
    while True:
        page_url = f"{category_url}?page={page_number}"
        listings_data = get_listings_data(page_url)

        if not listings_data:
            break

        for listing in listings_data:
            cross_reference = extract_cross_reference(listing["url"])
            if cross_reference is not None:
                listing["cross_reference"] = cross_reference

        duplicate_listings = find_duplicate_listings(listings_data)

        if duplicate_listings:
            print(f"Duplicate Listings Found in Category: {category_url}, Page: {page_number}")
            for listing in duplicate_listings:
                print(f"SKU: {listing['sku']}, Cross-Reference: {listing['cross_reference']}")
        else:
            print(f"No Duplicate Listings Found in Category: {category_url}, Page: {page_number}")

        page_number += 1

def navigate_subcategories(category_url):
    response = requests.get(category_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        subcategory_links = soup.find_all("a", class_="subcategory-link")

        if subcategory_links:
            for link in subcategory_links:
                subcategory_url = base_url + link.get("href")
                navigate_subcategories(subcategory_url)
        else:
            navigate_listings(category_url)

def main():
    navigate_subcategories(start_category_url)

if __name__ == "__main__":
    main()
