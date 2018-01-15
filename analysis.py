import operator 
import json
import preprocess
import string
from collections import Counter
from textblob import TextBlob

fname = 'tweets.json'

def averageSentiment():
	polarity_total = 0
	count = 0
	with open(fname, 'r') as file:
		for line in file:
			try:
				tweet= json.loads(line)
				#tokens = preprocess(tweet['text'])
				testimonial = tweet['text'] #access status only
				blob = TextBlob(testimonial)
				polarity_total = polarity_total + blob.sentiment.polarity
				count = count+1
				#print(testimonial)
			except BaseException as e:
				#print("Error: couldn't load JSON line")
				v = 1+1
				
	sentiment_polarity = polarity_total/count
	return sentiment_polarity
	
	
def individualSentiment():
	# Tweets are stored in "fname"
	with open(fname, 'r') as file:
		geo_data = {
			"features": []
		}
		for line in file:
			try:
				tweet = json.loads(line)
				geo_json_feature = {
					"geometry": tweet['coordinates'],
					"sentiment_polarity": TextBlob(tweet['text']).sentiment.polarity,
					"sentiment_subjectivity": TextBlob(tweet['text']).sentiment.subjectivity,
					"properties": {
						"text": tweet['text'],
						"location": tweet['user']['location'],
						"created_at": tweet['created_at']
					}
				}
				#json_line = {"id": data['id'],"testimonial": data['text'],"coordinates": data['coordinates'],"sentiment_polarity": TextBlob(testimonial).sentiment.polarity,"sentiment_subjectivity": TextBlob(testimonial).sentiment.subjectivity}
				geo_data['features'].append(geo_json_feature)
			except BaseException as e:
				#print("Error: couldn't load JSON line")
				v = 1+1
	print("successfully created json data file")
	with open('geo_data.json', 'w') as fout:
		fout.write(json.dumps(geo_data, indent=4))
	

individualSentiment()
print("average sentiment polarity: ", averageSentiment())


#with open(fname, 'r') as f:
#    count_all = Counter()
#    for line in f:
#        tweet = json.loads(line)
#        # Create a list with all the terms
#        terms_all = [term for term in preprocess(tweet['text'])]
        # Update the counter
#        count_all.update(terms_all)
    # Print the first 5 most frequent words
#    print(count_all.most_common(5))