import argparse

QUERY = None
SUBREDDIT = None
SORT = None
TIME = None

class ArgumentParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('--query', nargs='?', const='olympics OR #olympics OR #olympics2024 OR paris 2024 OR \
                                 paris2024 OR olympic games OR #olympicgames OR olympic day OR #olympicday OR road to \
                                 paris 2024 OR #roadtoparis2024 OR olympic 2024 OR #olympic2024 OR olympic OR #olympic \
                                 OR summer olympics OR #summerolympics OR 2024 paris olympics OR #2024parisolympics OR \
                                 paris olympics OR #parisolympics', help='Specify the search query. If used without a \
                                 value, is set to a default query. When this argument is absent,\
                                 the reddit search is performed globally not based on a query match.')
        self.parser.add_argument('--subreddit', type=str, default='olympics',  help='Can be set to the subreddit name. Default value is "olympics".')
        self.parser.add_argument('--sort', type=str, default='new', help='Can be set to "hot", "top", "new", "relevant", "comments".  Default value is "new".')
        self.parser.add_argument('--time', type=str, default='month', help='Can be set to , "hour", "day", "week", "month", "year", "all".  Default value is "month".')
        self.args = self.parser.parse_args()

    def get_values(self):
        query = self.args.query
        subreddit = self.args.subreddit
        sort = self.args.sort
        time = self.args.time
        return query, subreddit, sort, time