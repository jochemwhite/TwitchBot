 ######  ########   #######  ######## #### ######## ##    ## 
##    ## ##     ## ##     ##    ##     ##  ##        ##  ##  
##       ##     ## ##     ##    ##     ##  ##         ####   
 ######  ########  ##     ##    ##     ##  ######      ##    
      ## ##        ##     ##    ##     ##  ##          ##    
##    ## ##        ##     ##    ##     ##  ##          ##    
 ######  ##         #######     ##    #### ##          ##    
  

from os import name
import spotipy
from spotipy.client import Spotify
from spotipy.oauth2 import SpotifyOAuth
import sys
from pprint import pprint

def spotifyAPI(SpotifyOAuth):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="c1ecf639ba224ed9bb17eabd83c95f87",
                                                client_secret="e0815b2509684ebfad2900396a852661",
                                                redirect_uri="http://localhost:8888/callback",
                                                scope="user-read-private,user-read-playback-state,user-modify-playback-state"))
    return sp

play = spotifyAPI(SpotifyOAuth)



def current():
    artists = play.current_playback()['item']['artists'][0]['name']
    song =  play.current_playback()['item']['name']
    
    redeem = (f'{song} by {artists}')
    return redeem


def play_song(message):
    play.add_to_queue(uri=message)
    










    




    