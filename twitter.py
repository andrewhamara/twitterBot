############################
import tweepy              #
from tweepy import Client  #
from quote import getQuote #
############################

# So I don't need to put my keys on git :)

# If you want to reproduce this, put the keys in a file
# with the same name and in the same order as in main
def readKeyFile():
    with open("keys.txt") as f:
        return f.read().splitlines()


def tweet():
    API_KEY,     \
    API_SECRET,  \
    BEARER_TOKEN,\
    ACCESS_TOKEN,\
    ACCESS_SECRET = readKeyFile()

    client = tweepy.Client(bearer_token=BEARER_TOKEN,  \
                           consumer_key=API_KEY,       \
                           consumer_secret=API_SECRET, \
                           access_token=ACCESS_TOKEN,  \
                           access_token_secret=ACCESS_SECRET)

    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    api = tweepy.API(auth)

    quote = getQuote()
    while not quote:
        quote = getQuote()

    try:
        client.create_tweet(text=quote)
    except Exception as e:
        print(e)
        tweet()
        return
