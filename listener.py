import tweepy
#override tweepy.StreamListener to add logic to on_status
# The Status object contains the information about a tweet.
class Listener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.created_at, status.user.screen_name, status.user.name, '-', status.source)

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_error disconnects the stream
            return False

        # returning non-False reconnects the stream, with backoff.
