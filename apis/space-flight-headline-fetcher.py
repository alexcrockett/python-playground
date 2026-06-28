# This script fetches and prints articles from the following API
# https://api.spaceflightnewsapi.net/v4/docs/

# Imports required for the program to work
import json  # Required to read and format the response

import requests  # Required to process the API

# Create a variable that is the api
space_flight_api = "https://api.spaceflightnewsapi.net/v4/articles/?has_event=true&has_launch=true&is_featured=true&limit=3"

# Make a GET request to the API and store the response in a variable
space_flight_news = requests.get(space_flight_api).json()
response_json = space_flight_news

# Extract the 'results' key from the response JSON
articles = response_json["results"]
for article in articles:
    print(f"Title: {article['title']}")
    print(f"Summary: {article['summary']}")
    print("\nMore information below:\n")
    print(f"URL: {article['url']}")
    print(f"Image URL: {article['image_url']}")
    print(f"News Site: {article['news_site']}")
    print(f"Published At: {article['published_at']}")
    print(f"Updated At: {article['updated_at']}")
    print(f"Featured: {article['featured']}")
    print(
        f"Launches: {', '.join([launch['provider'] for launch in article['launches']])}"
    )
    print(f"Events: {', '.join([event['provider'] for event in article['events']])}")
    print("\n" + "-" * 50 + "\n")  # Print a separator between articles
