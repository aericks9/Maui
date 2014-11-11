import json, tweepy

filename = 'usertimeline.json'
READ = 'rb'
tweets = json.load(open(filename,READ))

#Which hashtags were used?

# Consumer keys and access tokens, used for OAuth
READ = 'rb'
WRITE = 'wb'
tokens = json.load(open('tokens.json',READ))   
 
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(tokens['consumer_key'], tokens['consumer_secret'])
auth.set_access_token(tokens['access_token'], tokens['access_token_secret'])

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

def print_location(obj):

    tweet = {}
    tweet['location'] = obj.user.location.encode('utf8')
    #tweet['time-zone'] = obj.user.time_zone
    #tweet['isGeo'] = obj.geo

    return tweet

TEXT=1
hashtags = [word for tweet in tweets for word in tweet['text'][TEXT].split() if '#' in word]
print hashtags

#Which tweet is most popular? (Which tweet has the most retweets?)
retweets = sorted(tweets,key = lambda tweet: tweet['retweet_count'],reverse=True)
#print retweets[0]

#Get location from tweet
locations = [tweet['location'] for tweet in tweets]
#print locations

#Get locations from those who retweeted the most popular tweet
most_popular_tweet = retweets[0]
try:
    locations_of_retweeters = api.retweets(most_popular_tweet['id'])
except:
    pass
print map(print_location,locations_of_retweeters)