# Portfolio Project Paris 2024 Sentiment: Analyzing Public Opinion on Twitter
## Twitter Data Extraction
For the Twitter data collection process the Basic X API v2 was used. This API version allows search of recent tweets from the last 7 days that match the given search query, supporting up to 60 requests / 15 mins per app with a maximum of 100 results per response. The month limit for retrieving posts is 10000.

### Tweets Fetching
Retweets were excluded from the database to ensure more accurate results of the sentiment analysis. Since tweets rarely include country, country_code, and place_id data, I chose not to collect this information. The user's location, which is commonly present, is sufficient for my purposes.
Due to excluded retweets, strict restrictions and a technical error in recording to the database, I managed to get only 330 posts and decided to switch to the Reddit API.

### Prerequisites
Python 3.x installed on your system.
Install the required dependencies:

    pip install -r requirements.txt

### Configuration
To authenticate with the Twitter API, API keys, access tokens and a bearer token should be provided. These should be securely stored in a .env file in the root directory.
Twitter API credentials are stored as follows:

    API_KEY='api_key'
    API_KEY_SECRET='api_key_secret'
    ACCESS_TOKEN='access_token'
    ACCESS_TOKEN_SECRET='access_token_secret'
    BEARER_TOKEN='bearer_token'

### Usage
Run the script as follows:

    python paris_2024.py

### References
[1]: Tweepy Documentation. Available at: https://docs.tweepy.org/en/stable

[2]: Parack, Suhem; Monticone, Pietro; Piper, Andy; Shaikh, Moin; Garcia, David. "Getting started with the Twitter API v2 for academic research." Available at: https://github.com/xdevplatform/getting-started-with-the-twitter-api-v2-for-academic-research

[3]: X Developer Platform. "Search Tweets. Introduction." Available at: https://developer.x.com/en/docs/twitter-api/tweets/search/introduction

[4]: X Developer Platform. "Search Tweets. Building queries for Search Posts." Available at: https://developer.x.com/en/docs/twitter-api/tweets/search/integrate/build-a-query#boolean

[5]: X Developer Platform. "Search Tweets. Recent search pagination." Available at: https://developer.x.com/en/docs/twitter-api/tweets/search/integrate/paginate

[6]: X Developer Platform. "Twitter API v2 data dictionary. Place." Available at: https://developer.x.com/en/docs/twitter-api/data-dictionary/object-model/place

[7]: X Developer Platform. "Twitter API v2 data dictionary. User." Available at: https://developer.x.com/en/docs/twitter-api/data-dictionary/object-model/user

[8]: X Developer Platform. "Twitter API v2 data dictionary. Tweet." Available at: https://developer.x.com/en/docs/twitter-api/data-dictionary/object-model/tweet