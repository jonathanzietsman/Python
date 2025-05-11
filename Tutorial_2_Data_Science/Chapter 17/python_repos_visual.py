# This program creates an interactive visualization of popular Python repositories
# It demonstrates API interaction, data processing, and interactive plotting

import requests  # For making HTTP requests to the GitHub API
import plotly.express as px  # For creating interactive visualizations

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
print(f"Complete results: {not response_dict['incomplete_results']}")  # Check if results are complete

# Extract and process repository information for visualization
repo_dicts = response_dict['items']  # Get list of repository dictionaries
repo_links, stars, hover_texts = [], [], []  # Lists to store data for the plot

# Process each repository's information
for repo_dict in repo_dicts:
    # Create clickable links for repository names
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"  # HTML link format
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])  # Number of stars
    
    # Create hover text with owner and description
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"  # HTML line break for formatting
    hover_texts.append(hover_text)

# Create the interactive bar chart
title = "Most-Starred Python Projects on GitHub"
labels = {'x': 'Repository', 'y': 'Stars'}
fig = px.bar(x=repo_links, y=stars, title=title, labels=labels, hover_name=hover_texts)

# Customize the chart appearance
fig.update_layout(
    title_font_size=28,           # Larger title
    xaxis_title_font_size=20,     # Larger x-axis label
    yaxis_title_font_size=20      # Larger y-axis label
)

# Customize the bars
fig.update_traces(
    marker_color='SteelBlue',     # Set bar color
    marker_opacity=0.6            # Make bars slightly transparent
)

# Save the interactive visualization as an HTML file
fig.write_html('repo_visual.html')  # Creates a self-contained webpage