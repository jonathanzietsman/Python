# This program fetches and displays a specific article from Hacker News
# It demonstrates API calls, JSON handling, and data formatting

import requests  # For making HTTP requests to the API
import json     # For handling JSON data

# Make an API call to Hacker News and store the response
url = "https://hacker-news.firebaseio.com/v0/item/31353677.json"  # URL for a specific article
r = requests.get(url)  # Send GET request to the API
print(f"Status code: {r.status_code}")  # Check if the request was successful

# Process and display the article data
response_dict = r.json()  # Convert JSON response to Python dictionary
response_string = json.dumps(response_dict, indent=4)  # Format JSON for readable output
print(response_string)  # Display the formatted article data