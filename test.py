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

# We import our access keys:
from credentials import *    # This will allow us to use the keys as variables

# API's setup:
def twitter_setup():
    """
    Utility function to setup the Twitter's API
    with our access keys provided.
    """
    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    # Return API with authentication:
    api = tweepy.API(auth)
    return api

# We create an extractor object:
extractor = twitter_setup()

KEYWORDS = ['Arsenal', 'Emery', 'Xhaka', 'Ozil']

tweets = tweepy.Cursor(extractor.user_timeline, screen_name='piersmorgan')
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

print("Total number of tweets about Arsenal: \n{} tweets.".format(len(useful_tweets)))

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

print("Average length of tweet: {} characters.".format(int(mean)))

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
# pie_chart = pd.Series(percent, index=sources, name='Sources')
# pie_chart.plot.pie(fontsize=11, autopct='%.2f', figsize=(6, 6))
# plt.show()

from textblob import TextBlob
import re

def clean_tweet(tweet):
    '''
    Utility function to clean the text in a tweet by removing 
    links and special characters using regex.
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def analize_sentiment(tweet):
    '''
    Utility function to classify the polarity of a tweet
    using textblob.
    '''
    analysis = TextBlob(clean_tweet(tweet))
    if analysis.sentiment.polarity > 0:
        return 1
    elif analysis.sentiment.polarity == 0:
        return 0
    else:
        return -1

# We create a column with the result of the analysis:
data['SA'] = np.array([ analize_sentiment(tweet) for tweet in data['Tweets'] ])

# We display the updated dataframe with the new column:
display(data.head(10))

# We construct lists with classified tweets:
pos_tweets = [ tweet for index, tweet in enumerate(data['Tweets']) if data['SA'][index] > 0]
neu_tweets = [ tweet for index, tweet in enumerate(data['Tweets']) if data['SA'][index] == 0]
neg_tweets = [ tweet for index, tweet in enumerate(data['Tweets']) if data['SA'][index] < 0]

# We print percentages:
print("Percentage of positive tweets: {}%".format(len(pos_tweets)*100/len(data['Tweets'])))
print("Percentage of neutral tweets: {}%".format(len(neu_tweets)*100/len(data['Tweets'])))
print("Percentage of negative tweets: {}%".format(len(neg_tweets)*100/len(data['Tweets'])))