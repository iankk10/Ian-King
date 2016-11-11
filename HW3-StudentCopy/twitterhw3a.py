# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.
import tweepy

# Unique code from Twitter
access_token = "298924039-9Qhl8wqli2Kp5e3a9dairm1oofmtjgru4ME3I0j8"
access_token_secret = "yQZheaTgNLu0X27bZTPfMyOAi3W6E1tc6mYbtXxAvfw4k"
consumer_key = "hBrPryhRbvaa4J2H5N5fNnQTm"
consumer_secret = "E1XkE0LKhZsbG1CSreXN2calbdt3WDWRn00fucUwdbmT6Pdiad"

# authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# text for update to use
update_text = "Go Blue"
# file name for upload
file_name = "media/mens_lacrosse.jpg"

# upload image with the status text and hashtags
api.update_with_media(file_name, "#USMI-206 #Proj3 " + update_text)
