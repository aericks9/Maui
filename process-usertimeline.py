import json, tweepy

filename = 'usertimeline.json'
READ = 'rb'
tweets = json.load(open(filename,READ))
#Which hashtags were used?

# Consumer keys and access tokens, used for OAuth
READ = 'rb'
WRITE = 'wb'
tokens = json.load(open('../tokens.json',READ))   
 
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

def serialize_tweepy_object(obj):
    tweet = {}
    tweet['id'] = obj.id 
    tweet['retweet_count'] = len(api.retweets(obj.id)) #Ceiling effect because max is 100
    tweet['author-name'] = obj.author.name.encode('utf8')
    tweet['screen-name'] = obj.author.screen_name.encode('utf8')
    tweet['created-at'] = obj.created_at.strftime('%m-%d-%Y')
    tweet['text'] = obj.text.encode('utf8')
    
    text = obj.text.encode('utf8')
    words = ''.join(c if c.isalnum() else ' ' for c in text).split()

    tweet['analysis'] = {}
    tweet['analysis']['tweet_length'] = len(text) 
    tweet['analysis']['word-count'] = len(words)

    tweet['location'] = obj.user.location.encode('utf8')
    tweet['time-zone'] = obj.user.time_zone
    tweet['isGeo'] = obj.geo

    tweet['retweet_count'] = obj.retweet_count
    tweet['favorite_count'] = obj.favorite_count

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
'''
#Get locations from those who retweeted the most popular tweet
most_popular_tweet = retweets[0]
try:
    locations_of_retweeters = api.retweets(most_popular_tweet['id'])
except:
    pass
print map(print_location,locations_of_retweeters)
 
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(tokens['consumer_key'], tokens['consumer_secret'])
auth.set_access_token(tokens['access_token'], tokens['access_token_secret'])

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

user_file = open('gagatimeline.json',WRITE)
user_text_file = open('gagatimeline.txt','a')
user_excel_file = open('gagatimeline.csv','a')
json_list = []
for tweet in tweepy.Cursor(api.user_timeline, id="ladygaga", include_rts=False).items(10):
    tweet = serialize_tweepy_object(tweet)
    json_list.append(tweet)

    user_text_file.write(tweet['text'] + '\n')
    user_excel_file.write(str(tweet['author-name']) + '|' + tweet['text'] + '|' + str(tweet['location']) + '|' + str(tweet['retweet_count']) + '|' + str(tweet['favorite_count']) + '\n')
'''
gagatweets = open('gagatimeline.txt',READ).read().splitlines()
hashtags = [[word for word in tweet if '#' in word] for tweet in gagatweets]
print hashtags