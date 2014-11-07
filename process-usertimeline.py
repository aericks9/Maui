import json

filename = 'usertimeline.json'
READ = 'rb'
tweets = json.load(open(filename,READ))

#Which hashtags were used?

TEXT=1
hashtags = [word for tweet in tweets for word in tweet['text'][TEXT].split() if '#' in word]
#print hashtags

#Which tweet is most popular? (Which tweet has the most retweets?)
#Need retweet field from Twitter
#print tweets

#Get location from tweet
locations = [tweet['location'] for tweet in tweets]
print locations