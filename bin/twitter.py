import tweepy
import json
from prettytable import PrettyTable
from cve_module import insert_newlines

followed_accounts = ['CVEnew', 'ExploitDB']

def create_twitter_api(json_file = '../conf/twitter_conf.json'):
    with open(json_file) as f:
        data = json.load(f)
    auth = tweepy.OAuthHandler(data['ApiKey'], data['ApiKeySecret'])
    auth.set_access_token(data['AccessToken'], data['AccessTokenSecret'])
    api = tweepy.API(auth)
    return api

def twitter(args):
    #Process keywords
    search_keywords = []
    if isinstance(args, list):
        search_keywords = ' '.join(str(i) for i in args)
    else:
        search_keywords = str(args)

    #Get twitter api
    api = create_twitter_api()
    
    #Get relevant information
    table = PrettyTable(['User', 'Tweet' ,'RT count', 'Date'])
    table.align = "l"
    
    for accs in followed_accounts:
        query = 'from:' + followed_accounts[0] + ' ' + search_keywords
        cursor = tweepy.Cursor(api.search_tweets, q=query, lang='en', count=10, tweet_mode="extended").items()
        for i in cursor:
            table.add_row([i.user.screen_name, insert_newlines(i.full_text,64), str(i.retweet_count), str(i.created_at)[:10]])
    
    cursor = tweepy.Cursor(api.search_tweets, q=search_keywords, lang='en', count=25, tweet_mode="extended").items()
    for i in cursor:
        table.add_row([i.user.screen_name, insert_newlines(i.full_text,64), str(i.retweet_count), str(i.created_at)[:10]])
    
    print(table)
