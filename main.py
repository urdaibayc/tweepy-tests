import tweepy

def get_credentials():
    # gets info from text file & returns a variable list
    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_token_secret = ''

    with open("credentials.txt") as fp:
        lines = fp.readlines()
        consumer_key = str(lines[1].strip())
        consumer_secret = str(lines[3].strip())
        access_token = str(lines[5].strip())
        access_token_secret = str(lines[7].strip())

    return [consumer_key, consumer_secret, access_token, access_token_secret]


def autenticate(credentials):
    # autenticates credentias to twtter & returns a tweepy auth object
    auth = tweepy.OAuthHandler(credentials[0], credentials[1])
    auth.set_access_token(credentials[2], credentials[3])
    return auth



#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_error disconnects the stream
            return False

        # returning non-False reconnects the stream, with backoff.

# Getting api credentials

credentials = get_credentials()
auth = autenticate(credentials)
api = tweepy.API(auth)

# Creating a Stream

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)


# Starting a Stream
myStream.filter(track=['python'])
# myStream.filter(track=['python'], is_async=True)
