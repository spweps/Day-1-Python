import requests

# Set the API endpoint and parameters
endpoint = "https://api.supplier.com/inventory"
params = {"product_id": "1234"}

# Send a GET request to the API endpoint
response = requests.get(endpoint, params=params)

# Check the response status code
if response.status_code == 200:
    # Parse the response JSON and extract the inventory quantity
    response_json = response.json()
    inventory_qty = response_json["inventory_quantity"]
    print(f"Inventory quantity for product 1234: {inventory_qty}")
else:
    print(f"Error: {response.status_code} - {response.text}")
