# YouTube Channel Scraper 📺🕵️

The YouTube Channel Scraper is a Python script that empowers you to effortlessly extract YouTube channel links from Google search results. Say goodbye to manual searching and hello to automation!

## How It Works 🛠️

1. The script sends GET requests to Google search and gracefully retrieves the search results.

2. It carefully extracts all the links from those search results.

3. The script cleverly filters out just the YouTube channel links and discards the rest. No clutter here!

4. It takes those filtered links and constructs complete URLs for the YouTube channels.

5. The extracted YouTube channel links are conveniently stored in both CSV and JSON formats for your convenience.

You can easily specify the search query and the maximum number of search results to retrieve. This script puts you in control! 🚀

## Usage 💡

1. Clone the repository or download the Python script. 📥

2. Install the required Python packages: requests, re, csv, json. 📦

3. Open the script in your favorite text editor and set the parameters:

   - MAX_RESULTS: Maximum number of search results to retrieve.
   - query: Search query for Google search. Customize it to match your search.
   
4. Run the script and watch it work its magic. ✨

The script will gracefully send requests to Google search and scrape the YouTube channel links. It saves the results in a CSV file (youtube_channels.csv) and a JSON file (youtube_channels.json).

After it's done, you'll be informed about the number of YouTube channel links that were gracefully scraped and saved.

## Notes 📝

- Make sure to comply with Google's terms of service and legal usage policies while using this script. Play by the rules!

- This script relies on the requests library for making HTTP requests and the re library for pattern matching.

- The CSV and JSON files provide flexibility in accessing and analyzing the scraped YouTube channel links. It's all about convenience!

- Feel free to customize and modify the code to fit your specific needs. The power is in your hands. 💪

Do you have questions or need assistance? Reach out, and we're here to help! 🙌
