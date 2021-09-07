from src.twitch.song.plugin import callback_whisper
from twitchAPI import PubSub
from twitchAPI.twitch import Twitch
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.types import AuthScope
from uuid import UUID
import os
import time
from twitchIO import Twitchy
import traceback








  # take environment variables from .env.

twitch = Twitch("f7pcaepc395qxkinldmueo6pbbpe31","pa961iup3dmnna94io6cyxcxc2agvo")
target_scope = [AuthScope.CHANNEL_READ_REDEMPTIONS]
auth = UserAuthenticator(twitch, target_scope, force_verify=False)
user_id = twitch.get_users(logins=['Jochemwhite'])['data'][0]['id']


# setting up Authentication and getting your user id

def Twitchbot():
  while True:
      twitchy = Twitchy()
      try:
        twitchy.loadPlugins()
        twitchy.connect(6667)
        twitchy.run()
      except Exception as e:
        print(traceback.format_exc())
      # If we get here, try to shutdown the bot then restart in 5 seconds
      twitchy.kill()
      time.sleep(5)



def twitch_token(twitch, auth, target_scope):
    # this will open your default browser and prompt you with the twitch verification website
    token, refresh_token = auth.authenticate()
    # add User authentication
    twitch.set_user_authentication(token, target_scope, refresh_token) 
    print(twitch_token)

    


def pubsub(twitch, user_id, callback_whisper):
    # starting up PubSub
    pubsub = PubSub(twitch)
    pubsub.start()
    # you can either start listening before or after you started pubsub.
    uuid = pubsub.listen_channel_points(user_id, callback_whisper)
    Twitchbot()


    



    


    input('press ENTER to close...')
    # you do not need to unlisten to topics before stopping but you can listen and unlisten at any moment you want
    pubsub.unlisten(uuid)
    pubsub.stop()


    



        
        


twitchAPI = twitch_token(twitch, auth, target_scope), pubsub(twitch, user_id, callback_whisper), 





