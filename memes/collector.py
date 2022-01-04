import praw
import os
import datetime

class Meme(object):
    id = 0
    subreddit = ""
    title = ""
    url = ""
    score = 0
    timestamp = datetime.datetime.now()
    video_url = ""

    def __init__(self, id, subreddit, title, url, score, timestamp):
        self.id = id
        self.subreddit = subreddit
        self.title = title
        self.url = url
        self.score = score
        self.timestamp = datetime.datetime.fromtimestamp(timestamp)

class RedditCollector:
    def __init__(self, client_id, client_secret, user_agent, limit, username, password):

        self.client_id = client_id
        self.client_secret = client_secret
        self.user_agent = user_agent
        self.limit = limit
        self.reddit = praw.Reddit(client_id=self.client_id, client_secret=self.client_secret,
                                  user_agent=self.user_agent, username=username, password=password)
        print(f'>>> Reddit User: {self.reddit.user.me()}')

    def collect_memes(self, subreddits):
        print('>>> Fetching subreddits data... \n\n')

        allowed_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.gifv']

        self.memes = []

        for subreddit_name in subreddits:

            subreddit = self.reddit.subreddit(subreddit_name)
            posts = subreddit.hot(limit=self.limit)
            for post in posts:
                _, ext = os.path.splitext(post.url)

                if ext in allowed_extensions:
                    meme = Meme(post.id, subreddit_name, post.title, post.url, post.score, post.created)
                    if ext == ".gif":
                        x = post.preview['images'][0]['variants']['mp4']['source']['url']
                        if x != None or x != "":
                            meme.video_url = x
                    self.memes.append(meme)

        return self.memes