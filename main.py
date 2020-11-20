
from listener import Listener
from autenticate import *

# TODO: import logging


def get_user(api, field):
    # str:: user_id, screen_name
    # digit:: user_id
    try:
        print(f'Searching for user {field}')
        user = api.get_user(field)
        print(f"Register for {field} -- foud: {user.name}")
    except tweepy.TweepError as e:
        print(e.response.status_code)
        #print(e.reason)


def main():
    api = get_api_object()
    ####################################
    ##### Create a stream of tweets ####
    ####################################
    # Creating a Stream
    StreamListener = Listener()
    Stream = tweepy.Stream(auth = api.auth, listener=StreamListener)
    # Starting a Stream
    Stream.filter(track=['python'])
    # myStream.filter(track=['python'], is_async=True)
    ####################################
    ##### Find User ####################
    ####################################
    # get_user(api, 162944864)

if __name__ == '__main__':
    main()
