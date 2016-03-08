import urllib
import os
from time import sleep
import tweepy
import api_keys

class TwitterAPI:
    def __init__(self, tweet_on, num_tries):
        self.tweet_on = tweet_on
        self.num_tries = num_tries
        consumer_key = api_keys.twitter_c_k
        consumer_secret = api_keys.twitter_c_s
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = api_keys.twitter_a_t
        access_token_secret = api_keys.twitter_a_t_secret
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def tweet(self, message):
        if(self.tweet_on):
            for i in range(self.num_tries):
                try:
                    self.api.update_status(status=message)
                    break
                except:
                    sleep(60)
        else:
            print("TWEET: " + message)

    def tweet_img(self, url, message):
        if(self.tweet_on):
            for i in range(self.num_tries):
                try:
                    urllib.urlretrieve(url, "img_upload.png")
                    fn = os.path.abspath("./img_upload.png")
                    self.api.update_with_media(fn, status=message)
                    break
                except:
                    sleep(60)
        else:
            print("IMAGE TWEET:" + message)
