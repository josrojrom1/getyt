from pytube import YouTube
import os
import time
from pytube.cli import on_progress

os.system('clear')

# banner
banner = open("banner.txt", "r")
print(banner.read())

print("\n")

time.sleep(1)

url=input("Paste here the URL to download (age restricted videos not allow yet)-> ")

downloadLocation="/home/tric0/Descargas"

print("\n")

while True:
    download_type = input("Type a/v if you want to download audio/video -> ")

    if download_type == "a" or download_type == "v":
        break
    else:
        print("Invalid argument -> " + download_type + ", please try again")




def download_audio(url,path):
    youtube=YouTube(url, on_progress_callback=on_progress)
    # we take only the video formats.
    # change progressive to only_audio for audio
    my_audio=youtube.streams.get_audio_only()
    yt_title=youtube.title
    print("Title: "+yt_title)


    while True:
        agreement= input(" Do you want to download audio? Type y/n -> ")
        if agreement == "y":
            break
        elif agreement == "n":
            return
        else:
            print("Invalid argument -> " + agreement + ", please try again")  

    # download the audio
    # progress bar
    print("Downloading audio [ "+yt_title+" ]...:")
    my_audio.download(output_path=path)
    print("Your audio is downloaded succesfully!")


    print("\n")

    time.sleep(1)
def download_video(url,path):
    youtube=YouTube(url, on_progress_callback=on_progress)
    # we take only the video formats.
    # change progressive to only_audio for audio
    my_video=youtube.streams.get_highest_resolution()
    yt_title=youtube.title
    print("Maximum resolution for: " + yt_title + "\n")
    
    # print avaible resolutions
    
    print("[ "+my_video.resolution+" ]")

    print("\n")

    time.sleep(1)

    while True:
        agreement= input(" Do you want to download video? Type y/n -> ")
        if agreement == "y":
            break
        elif agreement == "n":
            return
        else:
            print("Invalid argument -> " + agreement + ", please try again")

    # download the video
    # progress bar
    print("Downloading video [ "+yt_title+" ]...:")
    my_video.download(output_path=path)
    print("Your video is downloaded succesfully!")
    


if str(download_type)=="a":
    
    download_audio(url,downloadLocation)
elif str(download_type)=="v":
    download_video(url,downloadLocation)
else:
    print("Invalid argument -> "+download_type+", please try again")