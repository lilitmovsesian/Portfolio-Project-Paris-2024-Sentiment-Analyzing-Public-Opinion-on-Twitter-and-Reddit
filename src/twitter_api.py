import tweepy
from .database_manager import Tweet

class TwitterAPI:
    def __init__(self, api_key, api_key_secret, access_token, access_token_secret, bearer_token):
        self.client = tweepy.Client(bearer_token)
    
    def fetch_tweets(self, query):
        tweets = self.client.search_recent_tweets(query=query, tweet_fields=['id', 'text', 'created_at'], max_results=10)
        if tweets.data is None:
            return []
        return [Tweet(id = tweet.id,text=tweet.text, created_at=tweet.created_at) for tweet in tweets.data if not tweet.text.startswith('RT @')]