import tweepy
import json

def create_twitter_api(json_file = '../conf/twitter_conf.json'):
    with open(json_file) as f:
        data = json.load(f)
    auth = tweepy.OAuthHandler(data['ApiKey'], data['ApiKeySecret'])
    auth.set_access_token(data['AccessToken'], data['AccessTokenSecret'])
    api = tweepy.API(auth)
    return api

api = create_twitter_api()

cursor = tweepy.Cursor(api.search_tweets, q='CVE-2021-44228', lang='en', tweet_mode="extended").items(1)
for i in cursor:
    print(i.time)
    print(i.full_text)

#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print(tweet.text)
