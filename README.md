# Portfolio Project Paris 2024 Sentiment: Analyzing Public Opinion on Twitter and Reddit

## Twitter 

### Twitter Data Extraction Tools
For the Twitter data collection process the Basic X API v2 and 'Tweepy' library were used. This API version allows search of recent tweets from the last 7 days that match the given search query, supporting up to 60 requests / 15 mins per app with a maximum of 100 results per response. The month limit for retrieving posts is 10000.

### Tweets Fetching
Retweets were excluded from the database to ensure more accurate results of the sentiment analysis. Since tweets rarely include country, country_code, and place_id data, I chose not to collect this information. The user's location, which is commonly present, is sufficient for my purposes. The search query is:

    "olympics OR #olympics OR #olympics2024 OR paris 2024 OR #paris2024 OR olympic games OR #olympicgames OR olympic day OR #olympicday OR road to paris 2024 OR #roadtoparis2024 OR olympic 2024 OR #olympic2024 OR olympic OR #olympic OR summer olympics OR #summerolympics OR 2024 paris olympics OR #2024parisolympics OR paris olympics OR #parisolympics"



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

## Reddit 

Reddit is a popular social network, where users can write posts in different topics named 'subreddits'. Moreover, it contains advanced sorting options like hot, top, new, relevant and comments. Both these tools help in more advanced data search and sentiment analysis. Reddit API is widely used by users for sentiment analysis projects. 

### Reddit Posts Extraction Tools
Reddit posts were collected with use of Reddit API free version and 'PRAW' library, which allows to fetch up to 250 most recent posts per response based on the sort parameters provided.

### Reddit Posts Fetching
Reddit posts were searched through using several 'PRAW' functions, like 'subreddit.search' which searches by a given key-word query with different sorting parameters('hot', 'top', 'new', 'relevant', 'comments'), and 'subreddit.top', 'subreddit.hot', 'subreddit.new' functions, which search globally not based on a query match. The search was performed both in an 'all' subreddit based on a query and in a subreddit named 'olympics' without a query. The time filter was set to 'month', 'year' and 'all', but it was decided to exclude oldest posts within the data cleaning.

### Prerequisites
Python 3.x installed on your system.
Install the required dependencies:

    pip install -r requirements.txt

### Configuration
To authenticate with the client is, client secret and a user agent should be provided, which should be securely stored in a .env file in the root directory.
Reddit API credentials are stored as follows:

    CLIENT_ID = 'client_id'
    CLIENT_SECRET = 'client_secret'
    USER_AGENT = 'user_agent'

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

[9]: PRAW 7.7.1 documentation. "Authenticating via OAuth" Available at: https://praw.readthedocs.io/en/stable/getting_started/authentication.html

[10]: PRAW 7.7.1 documentation. "Subreddit." Available at: https://praw.readthedocs.io/en/stable/code_overview/models/subreddit.html