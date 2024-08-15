from src.reddit_api import RedditAPI
from src.database import Database
import os
from dotenv import load_dotenv

def main():
    load_dotenv()
    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')
    user_agent = os.getenv('USER_AGENT')

    reddit_api = RedditAPI(client_id, client_secret, user_agent)
    query = "olympics OR #olympics OR #olympics2024 OR paris2024 OR #paris2024 OR olympic games OR #olympicgames OR olympic day OR #olympicday OR road to paris 2024 OR #roadtoparis2024 OR olympic 2024 OR #olympic2024 OR olympic OR #olympic OR summer olympics OR #summerolympics OR 2024 paris olympics OR #2024parisolympics OR paris olympics OR #parisolympics"

    database = Database()
    session = database.get_session()

    posts = reddit_api.fetch_posts(query)
    database.add_posts(posts, session)
    
if __name__ == "__main__":
    main()