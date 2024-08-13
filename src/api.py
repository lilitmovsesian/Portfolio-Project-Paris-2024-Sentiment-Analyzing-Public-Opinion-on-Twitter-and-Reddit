import tweepy
import json

class TwitterAPI:
    def __init__(self, api_key, api_key_secret, access_token, access_token_secret):
        self.auth = tweepy.OAuth1UserHandler(api_key, api_key_secret, access_token, access_token_secret)
        self.api = tweepy.API(self.auth)