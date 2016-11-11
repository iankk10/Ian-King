# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.

import tweepy
from textblob import TextBlob

# Unique code from Twitter
access_token = "298924039-9Qhl8wqli2Kp5e3a9dairm1oofmtjgru4ME3I0j8"
access_token_secret = "yQZheaTgNLu0X27bZTPfMyOAi3W6E1tc6mYbtXxAvfw4k"
consumer_key = "hBrPryhRbvaa4J2H5N5fNnQTm"
consumer_secret = "E1XkE0LKhZsbG1CSreXN2calbdt3WDWRn00fucUwdbmT6Pdiad"

# authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# the search term
search_term = "2016 election"

results = api.search(search_term)

# count number of results returned
num_results = 0
# running count of subjectivity
total_subjectivity = 0
# running count of polarity
total_polarity = 0

for result in results:
    print("Tweet text: " + result.text)
    analysis = TextBlob(result.text)
    num_results += 1
    total_polarity += analysis.sentiment.polarity
    total_subjectivity += analysis.sentiment.subjectivity


print("Average subjectivity is: " + str(total_subjectivity/num_results))
print("Average polarity is: " + str(total_polarity/num_results))
