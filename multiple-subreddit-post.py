import praw
import os
import configparser

def reddit_authentication(config):
    config.read('auth.ini')
    redditClientId = config.get('credentials', 'reddit_Client_Id')
    redditClientSecret = config.get('credentials', 'reddit_Client_Secret')
    redditUsername = config.get('credentials', 'reddit_Username')
    redditPassword = config.get('credentials', 'reddit_Password')
    return praw.Reddit(client_id = redditClientId,
    client_secret = redditClientSecret,
    username = redditUsername,
    password = redditPassword,
    user_agent = 'multiple-subreddit_post')

class post_options():
    def __init__ (self, title, subreddit, url="", path="", flair="", inboxReplies = True, spoiler = False, originalContent = False, NSFW = False)
        self.inboxReplies = inboxReplies
        self.spoiler = spoiler
        self.subreddit = subreddit
        self.title = title
        self.originalContent = originalContent
        self.NSFW = NSFW
        self.url = url
        self.flair = "FLAIR CHOICES ON PRAW"


def multiple_subreddit_post():
    projectPath = os.path.dirname(os.path.realpath(__file__))
    authFile = projectPath + "/auth.ini"
    config = configparser.ConfigParser

    redditClient = reddit_authentication(config)
    subreddit = redditClient.subreddit("sub")

    for subreddit in subsToPost:
        redditClient.post(title = postOptions.title, spoiler = postOptions.spoiler, subreddit = postOptions.subreddit, is_original_content = postOptions.orignalContent, over_18 = postOptions.NSFW)
