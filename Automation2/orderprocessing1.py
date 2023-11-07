import requests
from bs4 import BeautifulSoup

def search_product(product_name, vendor_api_info):
    results = {}

    for vendor in vendor_api_info:
        if len(vendor) == 3:  # For API-based vendors
            vendor_name, api_key, api_url = vendor
            url = f"{api_url}?product={product_name}&apiKey={api_key}"
            response = requests.get(url)
            data = response.json()
            results[vendor_name] = data
        else:
            vendor_name, username, password, vendor_url = vendor
            scraped_data = scrape_vendor_data(username, password, vendor_url)
            if scraped_data:
                results[vendor_name] = scraped_data

    return results

def scrape_vendor_data(username, password, vendor_url):
    session = requests.Session()

    login_payload = {
        'username': username,
        'password': password,
        # Add other required login fields
    }

    login_response = session.post("https://vendor-login-url.com/login", data=login_payload)

    if login_response.status_code == 200:
        response = session.get(vendor_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract and process data using BeautifulSoup
        scraped_data = {}  # Placeholder, customize as needed
        # ...

        return scraped_data
    else:
        print("Login failed.")
        return None

def main():
    product_name = input("Enter the product name: ")

    vendor_info = [
        ("Vendor A (API)", "YOUR_VENDOR_A_API_KEY", "https://api.vendorA.com/search"),
        ("Vendor B (API)", "YOUR_VENDOR_B_API_KEY", "https://api.vendorB.com/search"),
        ("Vendor C (Login)", "username", "password", "https://vendorC.com/dashboard"),
        # Add more vendors (both API and login-based) here
    ]

    results = search_product(product_name, vendor_info)

    # Display results for all vendors
    for vendor, data in results.items():
        print(f"Results from {vendor}:")
        print(data)

if __name__ == "__main__":
    main()
