from creds import *
import tweepy
import time


def get_tweeet_api():
    auth = tweepy.OAuthHandler(consumer_key,consumer_seceret)

    auth.set_access_token(access_token,access_token_secret)

    tweet_api = tweepy.API(auth)
    return tweet_api


def get_tweets(tweet_api):

    public_tweets = tweet_api.home_timeline()

    print(len(public_tweets))

    for twt in public_tweets:
        print(twt.text)


def get_followers(tweet_api):

    followers = tweet_api.followers()
    print(len(followers))
    for f in followers:
        print(f.name)


def get_favourites(tweet_api):

    favourites = tweet_api.favorites()
    print(len(favourites))

    for twt in favourites:
        print("tweet by user : "+twt.user.name+" / "+twt.user.screen_name+" tweeted as : "+twt.text)



def tweet_from_file(file_path, tweet_api):
    try:
        with open(file_path,'r') as f:
            twt_lines = f.readlines()
        f.close()

        print(len(twt_lines))

        for twt_line in twt_lines:
            if (twt_line and twt_line != '\n'):
                print(twt_line)
                tweet_api.update_status(twt_line)
            time.sleep(10)

    except FileNotFoundError as err:
        print(err)
    except Exception as ex:
        print(ex)

def tweet_main():
    tweet_api = get_tweeet_api()
    # get_favourites(tweet_api)

    tweets_dt = tweepy.Cursor(tweet_api.search,q='#EOS_io').items(2)

    for twt in tweets_dt:
        print(twt.user.name)
        print(twt.text)
        twt.retweet()

tweet_main()