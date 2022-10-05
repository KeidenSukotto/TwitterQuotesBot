from bs4 import BeautifulSoup
import requests
import urllib.request
import os
import tweepy


# scrapping images sources

"""url = "https://www.azsonglyric.club/2019/02/5000-free-inspirational-quotes-to-learn.html"
website = requests.get(url)
markup = website.text

soup = BeautifulSoup(markup, "lxml")
anchor_tags = soup.find_all("a")
anchor_tags_with_images = [a for a in anchor_tags if a.has_attr("imageanchor")]

image_sources = [a.attrs["href"] for a in anchor_tags_with_images]"""


# downloading the images

"""count = 1

for source in image_sources:

    urllib.request.urlretrieve(source, fr"images/quote{count}.jpg")
    count += 1"""


# preparing an image to send

def retrieve_count():
    with open("count.txt") as file:
        count = int(file.readline())

    return count


def get_image():
    image = "images/quote{}.jpg".format(retrieve_count())

    return image


def increment_count():

    count = retrieve_count() + 1
    with open("count.txt", mode="w") as file:
        file.write(f"{count}")


# post on twitter

api_key = os.environ.get("api_key")
api_key_secret = os.environ.get("api_key_secret")
bearer_token = os.environ.get("bearer_token")
access_token = os.environ.get("access_token")
access_token_secret = os.environ.get("access_token_secret")

client = tweepy.Client(bearer_token, api_key, api_key_secret, access_token, access_token_secret)
authentication = tweepy.OAuth1UserHandler(api_key, api_key_secret, access_token, access_token_secret)
api = tweepy.API(authentication)


def create_tweet(image):

    media = api.media_upload(image)
    api.update_status(status="Quote of the day \n\n #positive #quote #inspirational #qouteoftheday #motivational", media_ids=[media.media_id])
    increment_count()


create_tweet(get_image())
