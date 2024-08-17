from src.reddit_api import RedditAPI
from src.database import Database
from src.argument_parser import ArgumentParser
import os
from dotenv import load_dotenv

def main():
    load_dotenv()
    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')
    user_agent = os.getenv('USER_AGENT')

    argument_parser = ArgumentParser()
    query, subreddit, sort, time = argument_parser.get_values()
    reddit_api = RedditAPI(client_id, client_secret, user_agent)
    database = Database()
    session = database.get_session()

    posts = reddit_api.fetch_posts(query, subreddit, sort, time)
    database.add_posts(posts, session)
    
if __name__ == "__main__":
    main()