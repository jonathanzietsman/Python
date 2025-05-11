# This program fetches and displays the top stories from Hacker News
# It demonstrates API interaction, data processing, and sorting

from operator import itemgetter  # For sorting dictionaries by values
import requests  # For making HTTP requests to the API

# Make an API call to get the list of top story IDs
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")  # Check if the request was successful

# Process information about each submission
submission_ids = r.json()  # Get list of story IDs
submission_dicts = []  # List to store information about each story

# Get details for the top 5 stories
for submission_id in submission_ids[:5]:
    # Make a separate API call for each story to get its details
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")  # Track API call status
    response_dict = r.json()  # Convert JSON response to dictionary
    
    # Create a dictionary with the information we want to display
    submission_dict = {
        'title': response_dict['title'],  # Story title
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",  # Link to story
        'comments': response_dict['descendants']  # Number of comments
    }
    submission_dicts.append(submission_dict)  # Add story info to our list

# Sort the stories by number of comments (most commented first)
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

# Display the sorted results
for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")