import tweepy
import json
from prettytable import PrettyTable
from cve_module import insert_newlines

def create_twitter_api(json_file = '../conf/twitter_conf.json'):
    with open(json_file) as f:
        data = json.load(f)
    auth = tweepy.OAuthHandler(data['ApiKey'], data['ApiKeySecret'])
    auth.set_access_token(data['AccessToken'], data['AccessTokenSecret'])
    api = tweepy.API(auth)
    return api

followed_accounts = ['CVEnew', 'ExploitDB']
cve_id = 'CVE-2022-25636'

api = create_twitter_api()

#Get relevant information
table = PrettyTable(['User', 'Tweet' ,'RT count', 'Date'])
table.align = "l"

for accs in followed_accounts:
    query = 'from:' + accs + ' ' + cve_id
    cursor = tweepy.Cursor(api.search_tweets, q=query, lang='en', count=10, tweet_mode="extended").items()
    for i in cursor:
        table.add_row([i.user.screen_name, insert_newlines(i.full_text,64), str(i.retweet_count), str(i.created_at)[:10]])

cursor = tweepy.Cursor(api.search_tweets, q=cve_id, lang='en', count=25, tweet_mode="extended").items()
for i in cursor:
    table.add_row([i.user.screen_name, insert_newlines(i.full_text,64), str(i.retweet_count), str(i.created_at)[:10]])

print(table)
