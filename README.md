# Inspirational Quote Twitter Bot

This Python script is designed to scrape inspirational quote images from a specific website, download them, and post them on Twitter using the Tweepy library.

## Scrapping Images Sources

The script begins by importing the necessary libraries, including BeautifulSoup for web scraping, requests for HTTP requests, urllib for image downloads, os for file operations, and tweepy for Twitter interaction.

It starts by sending an HTTP GET request to a predefined URL, "https://www.azsonglyric.club/2019/02/5000-free-inspirational-quotes-to-learn.html," and retrieves the website's markup. It then uses BeautifulSoup to parse the HTML content and extracts all anchor tags (`<a>`) that have an attribute named "imageanchor." These anchor tags likely contain the sources of the quote images on the webpage.

## Downloading Images

The script iterates through the list of anchor tags with image sources and downloads each image using `urllib.request.urlretrieve`. The images are saved with filenames like "quote1.jpg," "quote2.jpg," and so on, incrementing the count for each image.

## Managing Image Count

A set of functions is defined to manage the count of downloaded images. `retrieve_count` reads the count from a file named "count.txt." `get_image` constructs the filename of the next image to be posted based on the current count. `increment_count` updates the count in "count.txt" after posting an image.

## Posting on Twitter

The script requires Twitter API credentials, which are expected to be stored as environment variables: `api_key`, `api_key_secret`, `bearer_token`, `access_token`, and `access_token_secret`. It uses these credentials to authenticate with Twitter using Tweepy.

The `create_tweet` function takes the filename of the next image to post. It uploads the image to Twitter using `api.media_upload`, creates a tweet with a predefined status message and hashtags, and attaches the uploaded media to the tweet. After successfully posting the tweet, it calls `increment_count` to update the count for the next image.

## Execution

Finally, the script is executed by calling `create_tweet(get_image())`. This retrieves the next image to post, creates a tweet, and updates the count, ensuring that a new inspirational quote is shared on Twitter each time the script is run.
