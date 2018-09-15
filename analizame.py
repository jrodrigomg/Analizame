###Made by Rodrigo Mérida
###Twitter: joc_rodrigo

#importing libreries
import twitter
import json
import os
import re
import analize




hi = """
  ____  ____    ____  _      ____  _____   ____  ___ ___    ___ 
 /    ||    \\  /    || |    |    ||     | /    ||   |   |  /  _]
|  o  ||  _  ||  o  || |     |  | |__/  ||  o  || _   _ | /  [_ 
|     ||  |  ||     || |___  |  | |   __||     ||  \\_/  ||    _]
|  _  ||  |  ||  _  ||     | |  | |  /  ||  _  ||   |   ||   [_ 
|  |  ||  |  ||  |  ||     | |  | |     ||  |  ||   |   ||     |
|__|__||__|__||__|__||_____||____||_____||__|__||___|___||_____|
                                                                                                                 
"""

#user filter
USER = 'joc_rodrigo'

print (hi)
USER = input("Escribe el nickname del usuario en twitter que quieres analizar:\n")


#Get the configuration file
with open('config.json', 'r') as configfile:
    config = json.load(configfile)

#intialize the twitter api
api = twitter.Api(consumer_key=config["consumer_key"],
                  consumer_secret=config["consumer_secret"],
                  access_token_key=config["access_token_key"],
                  access_token_secret=config["access_token_secret"])


#rows to count.
MAX_COUNT = 200

#language filter
LANGUAGES = ['es', 'en']

#Open the file with the name of the user.
f = open("data_"+USER+".txt", "w+")

#Get the news for the user
# for line in api.GetStreamFilter(track=USERS, languages=LANGUAGES):
#     print (line) #printing line

#Get Timeline of users
statuses = api.GetUserTimeline(screen_name=USER, count=MAX_COUNT, include_rts=False, exclude_replies=True)

#separator
#f.write("\n\n\nUSER:"+USER+"\n\n\n")

#print the statuses on the file.
for s in statuses:
    #text = re.sub(r'^https?:\/\/.*[\r\n]*', '', s.text, flags=re.MULTILINE)
    #removing the urls... 
    text = re.sub(r'http\S+', '', s.text)
    #If is a RT or bot...
    if "RT" not in text and "unfollowed me" not in text:
        f.write(text+ "\r\n") 

#close the file
f.close()
configfile.close()
#analize!!!
analize.analizarTexto(USER)
#followers
#users = api.GetFriends()
#print([u.screen_name for u in users])


