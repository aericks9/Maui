import json
import matplotlib.pyplot as plt 
from textstat.textstat import textstat

from nltk import FreqDist


filename = 'bieber-raw-test.json'
READ = 'rb'
TEXT=1
stopwords = open('stopwords',READ).read().splitlines()
tweets = json.load(open(filename,READ))
#Identify retweets

words = ' '.join([tweet['text'] for tweet in tweets]).split()

fdist = FreqDist(words)

symbol,freq = zip(*fdist.most_common(20))


fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(freq,'k',linewidth=2)
ax.set_xticks(range(1,len(symbol)+1))
ax.set_xticklabels(symbol,rotation='vertical')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

plt.tight_layout()
plt.savefig('frequencies.png',dpi=300)