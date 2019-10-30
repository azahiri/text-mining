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

KEYWORDS = [
    'Arsenal', 'Emery', 'Xhaka', 'Ozil'
]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, acccess_token_secret)
api = tweepy.API(auth)
# for tweet in tweepy.Cursor(api.search,
#                            q="arsenal OR xhaka OR emery OR football from:piersmorgan",
#                            count=200,
#                            result_type="recent",
#                            include_entities=True,
#                            lang="en").items():
#                     print(tweet.created_at, tweet.text)

# tweets = api.user_timeline(screen_name='piersmorgan', count=3200)
# print(len(tweets))
# for tweet in tweets:
#     print(tweet.created_at, tweet.text)
# tweets = api.user_timeline(screen_name="piersmorgan", count=200)
# for tweet in tweets:
#     if "Arsenal" in tweet.text:
#         print(tweet.created_at, tweet.text)

tweets = tweepy.Cursor(api.user_timeline, screen_name='piersmorgan')

tweet_list = list(tweets.items())
# print(len(list(tweets.items())))

def process_tweets(tweets, keywords):
    """
    Given a list of tweets, a list of keywords,
    return a list of tweets that only contain the keywords
    """
    useful_tweets = []
    for tweet in tweets:
        for keyword in keywords:
            if keyword in tweet.text:
                useful_tweets.append(tweet.text)
                break
    return useful_tweets

useful_tweets = process_tweets(tweet_list, KEYWORDS)

# for tweet in useful_tweets:
#     print(tweet)

# print(useful_tweets)
# print(len(useful_tweets))    

def show_text(tweets):
    arsenal_tweet_text = []
    for tweet in useful_tweets:
        arsenal_tweet_text.append(tweet.text)
    return arsenal_tweet_text

def show_len(tweets):
    arsenal_tweet_len = []
    for tweet in useful_tweets:
        arsenal_tweet_len.append(len(tweet.text))
    return arsenal_tweet_len

def show_date(tweets):
    arsenal_tweet_date = []
    for tweet in useful_tweets:
        arsenal_tweet_date.append(tweet.created_at.strftime('%m/%d/%Y'))
    return arsenal_tweet_date

print(show_text(tweets1))
print(show_len(tweets2))
print(show_date(tweets3))



# We create a pandas dataframe as follows:
data = pd.DataFrame(data=show_text(useful_tweets), columns=['Tweets'])

# # We display the first 10 elements of the dataframe:
# display(data.head(10))

# We add relevant data:
data['len']  = np.array(show_len(useful_tweets))
data['ID']   = np.array([tweet.id for tweet in useful_tweets])
data['Date'] = np.array(show_date(useful_tweets))
data['Source'] = np.array([tweet.source for tweet in useful_tweets])
data['Likes']  = np.array([tweet.favorite_count for tweet in useful_tweets])
data['RTs']    = np.array([tweet.retweet_count for tweet in useful_tweets])

# Display of first 10 elements from dataframe:
display(data.head(10))

# We extract the mean of lenghts:
mean = np.mean(data['len'])

print("The lenght's average in tweets: {}".format(mean))

# print(arsenal_tweet_date)

# joined = arsenal_tweet_text + arsenal_tweet_date
# print(joined)
# We create a pandas dataframe as follows:
# data = pd.DataFrame(data=arsenal_tweet_date, columns=['Tweets'])

# # # We display the first 10 elements of the dataframe:
# display(data.head(10))

# # We add relevant data:
# # data['len']  = np.array(arsenal_tweet_len)
# # data['ID']   = np.array([tweet.id for tweet in tweets])
# data['Date'] = np.array(arsenal_tweet_date)
# data['Source'] = np.array([tweet.source for tweet in tweets])
# data['Likes']  = np.array([tweet.favorite_count for tweet in tweets])
# data['RTs']    = np.array([tweet.retweet_count for tweet in tweets])

# Display of first 10 elements from dataframe:
# display(data.head(10))

# We extract the mean of lenghts:
# mean = np.mean(data['len'])

# print("The lenght's average in tweets: {}".format(mean))

# # We print sources list:
# print("Creation of content sources:")
# for source in sources:
#     print("* {}".format(source))

# def create_dictionary(tweets):
#     """
#     Create a dictionary that includes only the necessary items from the twitter database.
#     We only need the unique ID and the actual tweets.
    
#     """
#     tweet_dictionary={}
#     for tweet in tweets.items():
#         # print(dir(tweet))
#         # print(tweet.text, tweet.id)
#         # print(dir(tweet.user))
#         # print(tweet.user.screen_name)
#         key = tweet.created_at
#         if key not in tweet_dictionary:
#             tweet_dictionary[key] = [tweet.text]
#         else: 
#             tweet_dictionary[key].append(tweet.text)
#     return tweet_dictionary

# print(create_dictionary(tweets.items()))

# dictionary_tweets = create_dictionary(tweets)



# tweets = api.user_timeline('realDonaldTrump')
# print(dir(tweets[0]))
# print(tweets[0].text)
# print(tweets[0].id, tweets[0].text, tweets[0].created_at)

# to print tweets
# CLEANS LIST OF DICTIONARY
# def clean_tweets(dictionary_tweets):
#     """
#     function that cleans the tweets 
#     this function removes the user id, url, and the 'RT' sign from 
#     the values of the dictionary tweets 
#     """
#     for key, value in dictionary_tweets.items():
#         count = 0
#         for word in value:
#             # print(words)
#             # print(type(words))
#             word = re.sub('@[^\s]+','',word) #gets rid of id 
#             word = remove_url(word) #gets rid of url
#             word = word.strip('RT') #get rid of rt
#             dictionary_tweets[key][count] = word
#             count += 1
#     # print(dictionary_tweets)
#     return dictionary_tweets

# cleaned_tweets = clean_tweets(dictionary_tweets)
# # print(cleaned_tweets)