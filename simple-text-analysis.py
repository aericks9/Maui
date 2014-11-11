import json

from textstat.textstat import textstat

filename = 'usertimeline.json'
READ = 'rb'
TEXT=1
stopwords = [word.rstrip('\r\n').strip() for word in open('stopwords',READ).readlines()]

tweets = json.load(open(filename,READ))
#Identify retweets
retweets = [word for tweet in tweets for word in tweet['text'][TEXT] if 'RT' in word]

print retweets
#identify replies

#Word count
print [tweet['analysis']['word-count'] for tweet in tweets]

#How would you do a character count?

#Lexical diversity
lex_div = lambda text: len(text.split())/float(len(set(text.split())))
print [lex_div(tweet['text'][TEXT]) for tweet in tweets]

#F-K

FK = []
for tweet in tweets:
	print tweet['text']
	try:
		FK.append(textstat.flesch_kincaid_grade(tweet['text']))
	except:
		FK.append(None)

print 'FK:', FK
#remove stopwords
print 'Removed stopwords:', [[word for word in tweet['text'].split() if word not in stopwords] for tweet in tweets]
#What's another way to filter out stopwords?
#How to handle punctuation?