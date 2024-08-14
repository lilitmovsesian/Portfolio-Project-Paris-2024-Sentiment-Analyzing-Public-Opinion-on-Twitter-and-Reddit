from src.twitter_api import TwitterAPI
from src.database_manager import DatabaseManager
import os
from dotenv import load_dotenv

def main():
    load_dotenv()
    api_key = os.getenv('API_KEY')
    api_key_secret = os.getenv('API_KEY_SECRET')
    access_token = os.getenv('ACCESS_TOKEN')
    access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
    bearer_token = os.getenv('BEARER_TOKEN')

    twitter_api = TwitterAPI(api_key, api_key_secret, access_token, access_token_secret, bearer_token)
    query = "olympics OR #olympics OR paris2024 OR #paris2024 OR olympic games OR #olympicgames OR olympic day OR #olympicday OR road to paris 2024 OR #roadtoparis2024 OR olympic 2024 OR #olympic2024"
    
    db_manager = DatabaseManager()
    session = db_manager.get_session()

    tweets = twitter_api.fetch_tweets(query)
    db_manager.add_tweets(tweets, session)

if __name__ == "__main__":
    main()