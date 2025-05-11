# This program fetches and displays information about popular Python repositories on GitHub
# It demonstrates API interaction, data filtering, and repository information display

import requests  # For making HTTP requests to the GitHub API

# Make an API call to GitHub's search endpoint
url = "https://api.github.com/search/repositories"
# Search for Python repositories with more than 10,000 stars, sorted by stars
url += "?q=language:python+sort:stars+stars:>10000"

# Set up headers to specify we want the v3 version of the API
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")  # Check if the request was successful

# Process the API response
response_dict = r.json()  # Convert JSON response to Python dictionary

# Display summary information about the search results
print(f'Total repositories: {response_dict["total_count"]}')  # Total number of matching repos
print(f'Complete results: {not response_dict["incomplete_results"]}')  # Check if results are complete

# Get the list of repositories from the response
repo_dicts = response_dict['items']  # List of repository dictionaries
print(f'Repositories returned: {len(repo_dicts)}')  # Number of repos in this response

# Display detailed information about each repository
print("\nSelected information about first repository:")
for repo_dict in repo_dicts:
    print(f"Name: {repo_dict['name']}")  # Repository name
    print(f"Owner: {repo_dict['owner']['login']}")  # Repository owner's username
    print(f"Stars: {repo_dict['stargazers_count']}")  # Number of stars
    print(f"Repository: {repo_dict['html_url']}")  # URL to the repository
    print(f"Created: {repo_dict['created_at']}")  # Creation date
    print(f"Updated: {repo_dict['updated_at']}")  # Last update date
    print(f"Description: {repo_dict['description']}")  # Repository description
    
    