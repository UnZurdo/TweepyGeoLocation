import json
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

#Enter Twitter API Key information
consumer_key= ''
consumer_secret= ''
access_token=''
access_secret=''
# 2 different outputs, 1 with the tweet info, and another just with the coordenates
file = open("Output3.csv", "w")
file2 = open("coordenadas.csv", "w")

data_list = []
count=0
class listener(StreamListener):

    def on_data(self, data):
    	global count
        #How many tweets you want to find
        if count <= 1000:
            json_data = json.loads(data)

            tweet = json_data["text"]
            username = json_data["user"]["screen_name"]

            coords = json_data["coordinates"] 
            if coords is not None:
 	           print coords["coordinates"]             
 	           print((username, tweet))
 	           print
 	           lon = coords["coordinates"][0]
 	           lat = coords["coordinates"][1]
 	           data_list.append(json_data) 
 	           file2.write(str(lon) + ",")
 	           file2.write(str(lat) + ",  "+ "\n")            
 	           file.write(str(lon) + ",")
 	           file.write(str(lat) + ",  ")
 	           file.write((username).encode('utf-8') + ",  ")
 	           file.write((tweet).encode('utf-8') + "\n")

 	           count += 1
 	           file.flush()	
 	           file2.flush()		
            return True
        else:
            file.close()
            return False

    def on_error(self, status):
        print status

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
twitterStream = Stream(auth, listener())
#What you want to search for here
#Location of my city [41.567414,-1.054222,41.707213,-0.760071])
twitterStream.filter(locations=[-1.054222,41.567414,-0.760071,41.707213])
