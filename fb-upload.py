#!/usr/local/bin/python3

## imports
import os
import time
import requests
import facebook
# from subprocess import call
#https://developers.facebook.com/docs/apps/review/server-to-server-apps/


#longlived access token

##get the files from Dropbox
#get the api key
keyfile = open("fbaccesstoken", "r")
keyline = keyfile.readline()
atoken = keyline.rstrip()




#page MiM: 257198117713783
#page Dash: 478769892607871

graph = facebook.GraphAPI(access_token=atoken)

print(graph)
print("-----------")

page = graph.get_object(id="257198117713783", fields="fan_count,website,about,name")

print(page)

resultt = graph.put_object( parent_object="257198117713783" , connection_name="feed", message="In Adversa Ultra Adversa")

# requests.post('', )

print(resultt)
