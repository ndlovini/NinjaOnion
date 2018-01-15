import json
import re

import operator 
import string
from collections import Counter

emoticons_str = r"""
	(?:
		[:=;] #eyes
		[oO\-]? # nose
		[D\)\]\(\]/\\OpP] # Mouth
	)"""
	
regex_str = [
	emoticons_str,
	r'<[^>]+>', # HTML tags
	r'(?:@[\w_]+)', # @-mentions
	r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
	r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
	r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
	r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
	r'(?:[\w_]+)', # other words
	r'(?:[\w_]+)', # other words
]

tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)

def tokenize(s):
    return tokens_re.findall(s)
 
def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens
 
#fname = 'tweets.json'
#with open(fname, 'r') as f:
    #count_all = Counter()
    #for line in f:
      #  tweet = json.loads(line)
        # Create a list with all the terms
    #    terms_all = [term for term in preprocess(tweet['text'])]
        # Update the counter
  #      count_all.update(terms_all)
    # Print the first 5 most frequent words
#    print(count_all.most_common(5))

#tweet = 'RT @marcobonzanini: just an example! :D http://example.com #NLP'
#print(preprocess(tweet))
	

#with open('tweets.json', 'r') as file:
#    for line in file:
#        tweet = json.loads(line)
#        tokens = preprocess(tweet['text'])
       # do_something_else(tokens)
	   
#if __name__ == "__main__":
#	import sys
#	tokenize(sys.argv)
#	preprocess(sys.argv)