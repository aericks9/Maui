import tweepy, io, json

from getpass import getpass

def serialize_tweepy_object(obj):
    tweet = {}
    tweet['author-name'] = obj.author.name.encode('utf8')
    tweet['screen-name'] = obj.author.screen_name.encode('utf8')
    tweet['created-at'] = obj.created_at.strftime('%m-%d-%Y')
    tweet['text'] = "Tweet:", obj.text.encode('utf8')
    
    text = obj.text.encode('utf8')
    words = ''.join(c if c.isalnum() else ' ' for c in text).split()

    tweet['analysis'] = {}
    tweet['analysis']['tweet_length'] = len(text) 
    tweet['analysis']['word-count'] = len(words)

    tweet['location'] = obj.user.location.encode('utf8')
    tweet['time-zone'] = obj.user.time_zone
    tweet['isGeo'] = obj.geo

    return tweet

# Consumer keys and access tokens, used for OAuth
READ = 'rb'
WRITE = 'wb'
tokens = json.load(open('tokens.json',READ))   
 
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(tokens['consumer_key'], tokens['consumer_secret'])
auth.set_access_token(tokens['access_token'], tokens['access_token_secret'])

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

user_file = open('med2tweets.json',WRITE)
json.dump([serialize_tweepy_object(tweet) 
        for tweet in tweepy.Cursor(api.search, q=('#med2'), since='2014-09-16', until='2014-11-02').items(3)], user_file)

