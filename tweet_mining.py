import json
import tweepy
import time
import string
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

consumer_key = "n8cEu9UAhB1w0O2PJW446m3h6"
consumer_secret = "8Sd9k5gTnZYh4V1iOhENHLrTmdCtO4UbG78xvSd4hbpRvlEaBX"
access_token = "2691204956-9C06mRSjd1PMIJDVrlVrr6P489oYtGDp36FLnVb"
access_secret = "zfxrM917UhwlZWCfZnv2mxS5PPPUjjTcC7QKrlbscqZPJ"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('tweets.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
		
if __name__ == "__main__":
	import sys
	search = str(sys.argv[1])
	twitter_stream = Stream(auth, MyListener())
	twitter_stream.filter(track=[search])