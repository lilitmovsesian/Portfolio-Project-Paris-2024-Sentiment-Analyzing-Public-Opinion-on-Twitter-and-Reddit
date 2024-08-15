import tweepy
from .database import Tweet
import time

class TwitterAPI:
    def __init__(self, api_key, api_key_secret, access_token, access_token_secret, bearer_token):
        self.client = tweepy.Client(bearer_token)
    
    def fetch_tweets(self, query):
        tweet_instances = []
        next_token = None
        for _ in range(1):
            tweets = self.client.search_recent_tweets(query=query, 
                                                    tweet_fields=['id', 'text', 'created_at'], 
                                                    user_fields = ['name','username','location','verified'], 
                                                    expansions = ['author_id'],
                                                    max_results = 100,
                                                    next_token = next_token)

            if tweets.data:
                users = {user['id']: user for user in tweets.includes['users']} if 'users' in tweets.includes else {}
                next_token = tweets.meta.get('next_token')
                for tweet in tweets.data:
                    if tweet.text.startswith('RT @'):
                        continue
                    id = tweet.id
                    text = tweet.text
                    created_at = tweet.created_at
                    author_id = tweet.author_id
                    name = None
                    username = None
                    location = None
                    verified = None

                    user = users.get(author_id)
                    if user:
                        name = user.get('name')
                        username = user.get('username')
                        location = user.get('location')
                        verified = user.get('verified')
                    tweet_instances.append(Tweet(id = id,text=text, created_at=created_at, author_id = author_id, name = name, username = username, location = location, verified = verified))
        return tweet_instances