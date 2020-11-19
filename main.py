import tweepy
from model import MyStreamListener


# TODO: import logging

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

def get_user_by_id(id):
    # using get_user with user_id
    try:
        print('Checking user id')
        user = api.get_user(id)
        print(f"The user id {id} corresponds to the user with the name: {user.name}")
    except ValueError:
        try:
            print('Checking user id as string')
            user = api.get_user(str(id))
            print(f"The user id {id} corresponds to the user with the name: {user.name}")
        except TweepError:
            print('Something whent wrong')





def get_user_by_screen_name(screen_name):
    # using get_user with screen_name
    user = api.get_user(screen_name)

    # printing the name of the user
    print("\nThe screen name " + screen_name +
          " corresponds to the user with the name : " +
          user.name)




def main():
    #####################################
    ##### Autenticate & api object ######
    #####################################
    # Getting api credentials
    credentials = get_credentials()
    auth = autenticate(credentials)
    # set up api object
    api = tweepy.API(auth)

    #####################################
    ###### Create a stream of tweets ####
    #####################################
    # # Creating a Stream
    # myStreamListener = MyStreamListener()
    # myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
    # # Starting a Stream
    # myStream.filter(track=['python'])
    # # myStream.filter(track=['python'], is_async=True)


if __name__ == '__main__':
    main()
