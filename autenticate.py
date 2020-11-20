import tweepy

def get_credentials():
    # gets info from text file & returns a variable list
    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_token_secret = ''
    try:
        print(f'Opening file: credentials.txt')
        with open("credentials.txt") as fp:
            lines = fp.readlines()
            consumer_key = str(lines[1].strip())
            consumer_secret = str(lines[3].strip())
            access_token = str(lines[5].strip())
            access_token_secret = str(lines[7].strip())
        return [consumer_key, consumer_secret, access_token, access_token_secret]
    except (IOError) as e:
        print(str(e))

def auth_object(credentials):
    # autenticates credentias to twtter & returns a tweepy auth object
    auth = tweepy.OAuthHandler(credentials[0], credentials[1])
    auth.set_access_token(credentials[2], credentials[3])
    return auth

def get_api_object():
    credentials = get_credentials()
    # Getting api credentials
    auth = auth_object(credentials)
    # set up api object
    return tweepy.API(auth)
