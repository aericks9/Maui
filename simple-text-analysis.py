import json

from textstat.textstat import textstat
from blessings import Terminal
from pprint import pprint 


terminal = Terminal()
filename = 'usertimeline.json'
READ = 'rb'
TEXT=1
stopwords = open('stopwords',READ).read().splitlines()
tweets = json.load(open(filename,READ))
#Identify retweets
retweets = [tweet['text'] for tweet in tweets if 'RT' in tweet['text']]

print terminal.bold(terminal.red('Retweets: ')),retweets
#identify replies
replies = [tweet['text'] for tweet in tweets if '@' in tweet['text']]
print terminal.bold(terminal.red('Replies: ')),replies
#Word count
print terminal.bold(terminal.red('Word count: ')),[tweet['analysis']['word-count'] for tweet in tweets]

#How would you do a character count?

#Lexical diversity
lex_div = lambda text: 1./round(len(text.split())/float(len(set(text.split()))),2)
print terminal.red(terminal.bold('Lexical diversity: ')),lex_div( ' '.join(tweet['text'] for tweet in tweets))

#F-K

FK = []
for tweet in tweets:
	try:
		FK.append(textstat.flesch_kincaid_grade(tweet['text']))
	except:
		FK.append(None)

print terminal.red(terminal.bold('FK:')), FK
#remove stopwords
print terminal.red(terminal.bold('With stopwords removed: ')), ' '.join([word for word in tweet['text'].split() 
									 							for tweet in tweets if word not in stopwords])
#What's another way to filter out stopwords?
#How to handle punctuation?

#---Recalculate after removing stopwrods
#Lexical diversity
without_stopwords = [' '.join([word for word in tweet['text'].split() if word not in stopwords]) for tweet in tweets]
print terminal.red(terminal.bold('Lexical diversity, without stopwords: ')),lex_div( ' '.join([tweet for tweet in without_stopwords]))

#F-K
FK = []
for tweet in without_stopwords:
	try:
		FK.append(textstat.flesch_kincaid_grade(tweet))
	except:
		FK.append(None)

print terminal.red(terminal.bold('FK without stopwords:')), FK
