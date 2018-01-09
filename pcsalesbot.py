import praw

reddit = praw.Reddit(client_id = 'X4IcGtfh-8RFOg',
                     client_secret = 'Q7TALZ1vm_Lls85Fy5b_EW5mTBU',
                     user_agent = 'BuildapcsalesWatcher:v0.1 (by /u/jtrot91)',
                     username = 'buildapcsaleswatcher',
                     password = 'password')

subreddit = reddit.subreddit('buildapcsales')

find = ['oculus', 'rift', 'vr', 'virtual reality', ]
found = False
for submission in subreddit.new(limit = 1):
    title = submission.title
    '''print(submission.id)
    print(submission.url)'''
    for check in find:
        if check in title.lower():
            found = True

