from .database import Post
import praw

class RedditAPI:
    def __init__(self, client_id, client_secret, user_agent):
        self.reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)
    
    def fetch_posts(self, query):
            
        subreddit_list = ['all']
        posts = []
        for subreddit_name in subreddit_list:
            subreddit = self.reddit.subreddit(subreddit_name)
            search_results = subreddit.search(query, sort='new', time_filter='year', limit=1000)
            
            for submission in search_results:
                id = submission.id
                title = submission.title
                text = None
                if submission.selftext:
                    text = submission.selftext
                url = submission.url
                score = submission.score
                subreddit_name = submission.subreddit.display_name
                author = submission.author.name
                created_at = submission.created_utc
                posts.append(Post(id = id,text=text, created_at=created_at, author = author, subreddit_name = subreddit_name, score = score, url = url, title = title))
        return posts