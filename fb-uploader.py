#!/usr/local/bin/python3

####
## AUTHOR: Federico De Faveri
## DATE: Sept 2018
## PURPOSE: script to fetch pics , process them and upload them to fb
####

## imports
import dropbox
import time

##get the files from Dropbox
#get the api key
keyfile = open("datafile", "r")
keyline = keyfile.readline()
apikey = keyline.rstrip()
# initialize dropbox client
print(">> Initializing Dropbox API")
dbx = dropbox.Dropbox(apikey)

for entry in dbx.files_list_folder('/fb-media-new').entries:
    timestamp = str(time.time()).split('.')[0]
    print(entry.name)
    print(entry.path_lower)
    # destpath = 
    # dbx.files_download_to_file(f'media/{timestamp}-{entry.path_lower}', entry.path_lower, rev=None)

# print(dir(dbx))


#for each file:
