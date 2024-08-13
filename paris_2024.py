from src.api import TwitterAPI
import os
from dotenv import load_dotenv

def main():
    load_dotenv()
    api_key = os.getenv('API_KEY')
    api_key_secret = os.getenv('API_KEY_SECRET')
    access_token = os.getenv('ACCESS_TOKEN')
    access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
        
    twitter_api = TwitterAPI(api_key, api_key_secret, access_token, access_token_secret)

if __name__ == "__main__":
    main()