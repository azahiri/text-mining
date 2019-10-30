# General:
import tweepy           # To consume Twitter's API
import pandas as pd     # To handle data
import numpy as np      # For number computing

# For plotting and visualization:
from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns
'exec(%matplotlib inline)'
import time
import datetime

#authenticate the keys 
consumer_key = 'UWWq3Sfkk89IPHiMIW3geSgXS'
consumer_secret = '9YcxuR1QoxS81FEEnY7FpA76G98j3q31fhl7MT0i55rFMGmV7W'
access_token = '1041370203563732992-pnt2lwFytx0JBfaC3Mgpr9XlZ60m7F' 
acccess_token_secret = 'D2PqFSBeLzjHelCqMKHvipr5vHcWhkdCJH9S4CWGsQkwS'

KEYWORDS = ['Arsenal', 'Emery', 'Xhaka', 'Ozil']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, acccess_token_secret)
api = tweepy.API(auth)

tweets = tweepy.Cursor(api.user_timeline, screen_name='piersmorgan')
tweet_list = list(tweets.items())

def process_tweets(tweets, keywords):
    """
    Given a list of tweets, a list of keywords,
    return a list of tweets that only contain the keywords
    """
    useful_tweets = []
    for tweet in tweets:
        for keyword in keywords:
            if keyword in tweet.text:
                useful_tweets.append(tweet)
                break
    return useful_tweets

useful_tweets = process_tweets(tweet_list, KEYWORDS)

# print(useful_tweets)
# print(len(useful_tweets))    


def show_count(tweets):
    count = 0
    for tweet in tweets:
        count += 1
    return count

def show_text(tweets):
    arsenal_tweet_text = []
    for tweet in tweets:
        arsenal_tweet_text.append(tweet.text)
    return arsenal_tweet_text

def show_len(tweets):
    arsenal_tweet_len = []
    for tweet in tweets:
        arsenal_tweet_len.append(len(tweet.text))
    return arsenal_tweet_len

def show_date(tweets):
    arsenal_tweet_date = []
    for tweet in tweets:
        arsenal_tweet_date.append(tweet.created_at.strftime('%m/%d/%Y'))
    return arsenal_tweet_date

def show_ID(tweets):
    arsenal_tweet_text = []
    for tweet in tweets:
        arsenal_tweet_text.append(tweet.id)
    return arsenal_tweet_text

def show_source(tweets):
    arsenal_tweet_text = []
    for tweet in tweets:
        arsenal_tweet_text.append(tweet.source)
    return arsenal_tweet_text

def show_likes(tweets):
    arsenal_tweet_text = []
    for tweet in tweets:
        arsenal_tweet_text.append(tweet.favorite_count)
    return arsenal_tweet_text

def show_RT(tweets):
    arsenal_tweet_text = []
    for tweet in tweets:
        arsenal_tweet_text.append(tweet.retweet_count)
    return arsenal_tweet_text

# print(show_count(useful_tweets))
# print(show_text(useful_tweets))
# print(show_len(useful_tweets))
# print(show_date(useful_tweets))

useful_tweets_text = show_text(useful_tweets)
useful_tweets_len = show_len(useful_tweets)
useful_tweets_date = show_date(useful_tweets)
useful_tweets_ID = show_ID(useful_tweets)
useful_tweets_source = show_source(useful_tweets)
useful_tweets_likes = show_likes(useful_tweets)
useful_tweets_RT = show_RT(useful_tweets)

# # We create a pandas dataframe as follows:
data = pd.DataFrame(data=useful_tweets_text, columns=['Tweets'])

# # We add relevant data:
data['len']  = np.array(useful_tweets_len)
data['ID']   = np.array(useful_tweets_ID)
data['Date'] = np.array(useful_tweets_date)
data['Source'] = np.array(useful_tweets_source)
data['Likes']  = np.array(useful_tweets_likes)
data['RTs']    = np.array(useful_tweets_RT)

# # Display of first 10 elements from dataframe:
display(data.head(10))

# # We extract the mean of lenghts:
mean = np.mean(data['len'])

print("The lenght's average in tweets: {}".format(int(mean)))

# We extract the tweet with more FAVs and more RTs:

fav_max = np.max(data['Likes'])
rt_max  = np.max(data['RTs'])

fav = data[data.Likes == fav_max].index[0]
rt  = data[data.RTs == rt_max].index[0]

# Max FAVs:
print("The tweet with the most likes is: \n{}".format(data['Tweets'][fav]))
print("Number of likes: {}".format(fav_max))
print("{} characters.\n".format(data['len'][fav]))

# Max RTs:
print("The tweet with the most retweets is: \n{}".format(data['Tweets'][rt]))
print("Number of retweets: {}".format(rt_max))
print("{} characters.\n".format(data['len'][rt]))

# We create time series for data:

tlen = pd.Series(data=data['len'].values, index=data['Date'])
tfav = pd.Series(data=data['Likes'].values, index=data['Date'])
tret = pd.Series(data=data['RTs'].values, index=data['Date'])

# Lenghts along time:
tlen.plot(figsize=(16,4), color='r')
plt.show()

# Likes vs retweets visualization:
tfav.plot(figsize=(16,4), label="Likes", legend=True)
tret.plot(figsize=(16,4), label="Retweets", legend=True)
plt.show()

# We obtain all possible sources:
sources = []
for source in data['Source']:
    if source not in sources:
        sources.append(source)

# We print sources list:
print("Creation of content sources:")
for source in sources:
    print("* {}".format(source))

# We create a numpy vector mapped to labels:
percent = np.zeros(len(sources))

for source in data['Source']:
    for index in range(len(sources)):
        if source == sources[index]:
            percent[index] += 1
            pass

percent /= 100

# Pie chart:
pie_chart = pd.Series(percent, index=sources, name='Sources')
pie_chart.plot.pie(fontsize=11, autopct='%.2f', figsize=(6, 6))
plt.show()