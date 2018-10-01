#!/usr/local/bin/python3

####
## AUTHOR: Federico De Faveri
## DATE: Sept 2018
## PURPOSE: script to fetch pics , process them and upload them to fb
####

## imports
import os
import dropbox
import time
import requests
from subprocess import call

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
    filename = entry.name
    filepath = entry.path_lower
    destpath = f'media/{timestamp}-{filename}'
    dbx.files_download_to_file( destpath, filepath, rev=None)

print("> Downloaded media files from Dropbox")

# apply watermarks
mediasource = []
for watermark in os.listdir('./watermarks'):
    print(f"> Applying watermark {watermark}")
    path = f"./ready-media/{watermark}"
    mediasource.append(path)
    call(["mkdir", path])
    for filename in os.listdir('./media'):
        if filename != ".DS_Store":
            call(["composite", "-dissolve", "40", "-gravity", "SouthEast", "-geometry", "+0+0", "watermarks/watermark1.png", f"media/{filename}", f"./ready-media/{watermark}/{filename}"])
            print(filename + " -> Watermarked")
        else:
            pass

# images with watermarks created

for filename in os.listdir('./ready-media'):
    print(f"now post {filename} to FB!")
