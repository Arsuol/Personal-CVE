import praw
import json
from prettytable import PrettyTable
from datetime import datetime
from cve_module import insert_newlines

cve_id = 'CVE-2022-24307'

def create_reddit_obj(json_file = '../conf/reddit_conf.json'):
    with open(json_file) as f:
        data = json.load(f)
    reddit = praw.Reddit(
        client_id       = data['client_id'], 
        client_secret   = data['client_secret'], 
        password        = data['password'], 
        username        = data['username'], 
        user_agent      = data['user_agent'], 
    )
    return reddit

#Global Variables
post_num = 25 #Maximum number of posts to display
table = PrettyTable(['Source', 'Posted' ,'Title', 'url'])
table.align = "l"

reddit = create_reddit_obj()

all = reddit.subreddit("all")
for i in all.search(cve_id, post_num):
    src = '/r/' + str(i.subreddit)
    time = str(datetime.fromtimestamp(i.created)).replace(' ', '\n')
    title = insert_newlines(i.title, 50)
    table.add_row([src, time, title, i.url])

print(table)
