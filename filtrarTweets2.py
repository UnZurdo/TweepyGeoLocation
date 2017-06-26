import json
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

#Enter Twitter API Key information
consumer_key= 'l2EF8otpmNPXVQy8bXp7lSkZH'
consumer_secret= 'v1Xr0dEYqLv9pVF985Cg9hf1WIfqOLszjz6npdRJMdimQ911pe'
access_token='2723252692-LpDhLkKBUzx79283gDwA4Jg3uoGGz1ED2K5cIdY'
access_secret='94qwUPMLK4rbynJaOZgxYQhK1i8LEiw7Po9arTBhhD9iO'

file = open("Output2.csv", "w")

data_list = []
count=0
class listener(StreamListener):

    def on_data(self, data):
    	global count
        #How many tweets you want to find, could change to time based
        if count <= 10:
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
 	           file.write(str(lon) + ",")
 	           file.write(str(lat) + ",  ")
 	           file.write(str(username) + ",  ")
 	           file.write(str(tweet) + "\n")

 	           count += 1	
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
#twitterStream.filter(locations=[41.567414,-1.054222,41.707213,-0.760071])
twitterStream.filter(locations=[-1.054222,41.567414,-0.760071,41.707213])
