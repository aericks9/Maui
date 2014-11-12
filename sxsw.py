import json

from textstat.textstat import textstat

from nltk import FreqDist
from matplotlib.pyplot import *

filename = 'bieber-raw-test.json'
READ = 'rb'
TEXT=1
stopwords = open('stopwords',READ).read().splitlines()
tweets = json.load(open(filename,READ))
#Identify retweets

words = ' '.join([tweet['text'] for tweet in tweets]).split()

fdist = FreqDist(words)

fdist.plot(20)
tight_layout()