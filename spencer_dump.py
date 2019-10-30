

########## some other shit

# def make_dict(tweets):
#     dictionary = dict()
#     for tweet in tweets.items():
#         dictionary[tweet.created_at] = tweet.text
#     return dictionary

# def arsenal_tweets(tweets):
#     count = 0
#     for tweet in tweets.items():
#         if "Arsenal" in tweet.text or "Emery" in tweet.text or "Xhaka" in tweet.text or "Ozil" in tweet.text:
#             count += 1
#             print(tweet.created_at, tweet.text)
        # print(arsenal_tweets[-1:])
# print(count)
# arsenal_tweets(tweets)

# def Convert(tup, di): 
#     for a, b in tup: 
#         di.setdefault(a, []).append(b) 
#     return di 
# tweet_dictionary = {}
# print(Convert(arsenal_tweets(tweets), tweet_dictionary))