from uuid import UUID
from src.API.twitchIO import Twitchy
from src.twitch.BasePlugin import BasePlugin






def callback_whisper(twitchy, uuid: UUID, response: dict):    
	id = (response['data']['redemption']['reward']['id']) #ID of the channelpoints thats redeemd  

	if(id =='94cf0eff-551e-478f-89d5-3276e52f8b60'):
	# userinput = (response['data']['redemption']['user_input'])
	# play.add_to_queue(uri=userinput)
		print('trying...')
		
		print('done')
		
		


class song(BasePlugin):
	def __init__(self, twitchy):
		super(song, self).__init__(twitchy)

		self.registerCommand('song', self.song) 
		self.registerTrigger('hey', self.heyHandler)
		
		 
		


	
	def song(self, nick, commandArg):
		self.sendMessage("Hello "+ nick +"!")
	
	def heyHandler(self, nick, fullMsg):
		self.sendMessage("Hey there, "+nick)
	
