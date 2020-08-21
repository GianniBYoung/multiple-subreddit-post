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



class post_options:
    def __init__(self, title, subreddits, url = '', path = '', flair = '', inboxReplies = True, spoiler = False, originalContent = False, NSFW = False):
        self.inboxReplies = inboxReplies
        self.spoiler = spoiler
        self.subreddits = subreddits
        self.title = title
        self.originalContent = originalContent
        self.NSFW = NSFW
        self.url = url
        self.flair = flair 

def select_subreddits:
    #function to select subreddits

def create_post():
    title = input('Enter Title: ')
    url = input('Enter url (leave blank if using path): ')
    path = input('Enter Path (leave blank if using url): ')
    flair = ''

    inboxReplies = input('Disable Inbox Replies? (y/n): ')
    if inboxReplies == 'y':
        inboxReplies = False
    else:
        inboxReplies = True

    spoiler = input('Enable Spoiler? (y/n): ')
    if spoiler == 'y':
        spoiler = True
    else:
        spoiler = False

    originalContent = input('Mark as OC? (y/n): ')
    if originalContent == 'y':
        originalContent = True
    else:
        originalContent = False

    NSFW = input('Mark as NSFW? (y/n): ')
    if NSFW == 'y':
        NSFW = True
    else:
        NSFW = False
    
    subreddits = [line.strip() for line in open("subredditList.txt", 'r')]

    return post_options(title, subreddits, url, path, flair, inboxReplies, spoiler, originalContent, NSFW)



def multiple_subreddit_post():
    projectPath = os.path.dirname(os.path.realpath(__file__))
    authFile = projectPath + "/auth.ini"
    config = configparser.ConfigParser()

    redditClient = reddit_authentication(config)
    data = {'spoiler': 'True'}
    postOptions = create_post()
    print(postOptions.url)
    for subreddit in postOptions.subreddits:
        subToPostTo = redditClient.subreddit(subreddit)
        submission = subToPostTo.submit(title = postOptions.title, url = postOptions.url)

        if not postOptions.inboxReplies:
            submission.disable_inbox_replies()

        if postOptions.spoiler:
            submission.mod.spoiler()

        if postOptions.NSFW:
            submission.mod.nsfw()
        else:
            submission.mod.sfw()

        if postOptions.originalContent:
            submission.mod.set_original_content()
multiple_subreddit_post()
