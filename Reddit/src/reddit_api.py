from .database import Post
import praw

class RedditAPI:
    def __init__(self, client_id, client_secret, user_agent):
        self.reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)
    
    def fetch_posts(self, query, subreddit_name, sort, time):      
        posts = []
        search_results = None
        subreddit = self.reddit.subreddit(subreddit_name)
        if query:
            search_results = subreddit.search(query, sort, time, limit=250)
        else:
            if sort == "top":
                search_results = subreddit.top(time, limit=250)
            elif sort == "hot":
                search_results = subreddit.hot(limit=250)
            elif sort == "new":
                search_results = subreddit.new(limit=250)

        if search_results is None:
            return []
        
        for submission in search_results:
            id = submission.id
            title = submission.title
            text = None
            if submission.selftext:
                text = submission.selftext
            url = submission.url
            score = submission.score
            subreddit_name = submission.subreddit.display_name
            author = None
            if submission.author:
                author = submission.author.name
            created_at = submission.created_utc
            posts.append(Post(id = id,text=text, created_at=created_at, author = author, subreddit_name = subreddit_name, score = score, url = url, title = title))
        return posts