import tweepy
from textblob import TextBlob

consumer_key = 	'bbmYmDymwRrWUnriAr1zHLUCC'
consumer_secret = '3VMEOQ7sGVH9VHCSMlZpqrxvXPoemLwWoG1y0Y9xFQhJiIShg5'

access_token = '943590451243728896-7OLlYkDsffzm4FGWVJUWOw35qCNsYBs'
accest_token_secret = 'r1YGQQ3mPIoLP3kGpPOkhGLiOCBRz8vsI2UzA7rZ0HFVc'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, accest_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('money')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
