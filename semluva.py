import tweepy
import time

CONSUMER_KEY = # hidden for obvious reasons
CONSUMER_SECRET = # hidden for obvious reasons
ACCESS_KEY = # hidden for obvious reasons
ACCESS_SECRET = # hidden for obvious reasons

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

twitter_API = tweepy.API(auth)

while True:
    twitter_API.update_status('#semluva')
    time.sleep(3600)
