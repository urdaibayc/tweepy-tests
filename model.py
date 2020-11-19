import tweepy

#override tweepy.StreamListener to add logic to on_status
# The Status object contains the information about a tweet.
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(type(status))

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_error disconnects the stream
            return False

        # returning non-False reconnects the stream, with backoff.
