import requests
import re
import csv
import json

# Set the maximum number of search results to retrieve
MAX_RESULTS = 10000

# Set the search query
query = 'site:youtube.com openinapp.co'

# Initialize the result list
results = []

# Generate the URL for Google search
url = f"https://www.google.com/search?q={query}&num=100"

# Set the headers to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# Send requests to Google and retrieve search results
while len(results) < MAX_RESULTS:
    # Send a GET request to Google search
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Extract all links from the search results
        links = re.findall(r'href="([^"]+)"', response.text)

        # Filter the links to keep only YouTube channel links
        youtube_channels = [link for link in links if '/channel/' in link]

        # Extract the YouTube channel URLs
        youtube_channel_urls = [re.search(r'/channel/([^/]+)', channel).group(1) for channel in youtube_channels]

        # Construct the complete YouTube channel URLs
        youtube_channel_urls = ['https://www.youtube.com/channel/' + channel for channel in youtube_channel_urls]

        # Add the YouTube channel URLs to the results list
        results.extend(youtube_channel_urls)

    # Check if we have reached the maximum number of search results
    if len(results) >= MAX_RESULTS:
        break

    # Extract the URL of the next page of search results
    next_page_url_match = re.search(r'href="([^"]+)"[^>]*aria-label="Next page"', response.text)
    if next_page_url_match:
        next_page_url = next_page_url_match.group(1)
        url = "https://www.google.com" + next_page_url
    else:
        break

# Truncate the results list to the maximum number of search results
results = results[:MAX_RESULTS]

# Write the results to a CSV file
with open('youtube_channels.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['YouTube Channel'])
    writer.writerows([[link] for link in results])

# Write the results to a JSON file
with open('youtube_channels.json', 'w', encoding='utf-8') as jsonfile:
    json.dump(results, jsonfile)

print(f"Scraped {len(results)} YouTube channel links and saved the results to 'youtube_channels.csv' and 'youtube")
