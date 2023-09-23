from pytube import YouTube
import os
import time
from pytube.cli import on_progress

#-------------------------------------------------------------
os.system('clear')

#-------BANNER-------------------------------------------------
banner = open("banner.txt", "r")
print(banner.read())
print("\n")
time.sleep(1)
#-------FIRST INPUT--------------------------------------------
url=input("Insert URL -> ")

#-------DOWNLOADS FOLDER PATH----------------------------------
def get_downloads_folder_path():
  #Returns the download path of your os

    if os.name == "nt":
    # Windows
        return os.path.join(os.getenv("USERPROFILE"), "Downloads")
    else:
    # Linux o macOS
        return os.path.join(os.path.expanduser("~"), "Downloads")

#-------DOWNLOAD PATH VARIABLE---------------------------------
download_location = get_downloads_folder_path()
print("\n")

#-------DOWNLOAD AUDIO/VIDEO OPTIONS----------------------------
while True:
    download_type = input("Type a/v if you want to download audio/video -> ")

    if download_type == "a" or download_type == "v":
        break
    else:
        print("Invalid argument -> " + download_type + ", please try again")

#-------DOWNLOAD AUDIO FUNCTION----------------------------------
def download_audio(url,path):
    youtube=YouTube(url, on_progress_callback=on_progress, use_oauth=True,allow_oauth_cache=True)
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

    # download the audio and progress bar
    print("Downloading audio [ "+yt_title+" ]...:")
    my_audio.download(output_path=path)
    print("Your audio is downloaded succesfully!")
    print("\n")
    time.sleep(1)

#-------DOWNLOAD VIDEO FUNCTION----------------------------------
def download_video(url,path):
    youtube=YouTube(url, on_progress_callback=on_progress, use_oauth=True,allow_oauth_cache=True)
    my_video=youtube.streams.get_highest_resolution()
    yt_title=youtube.title
    print("Maximum resolution for: " + yt_title + "\n")
    # print maximum resolution
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
            print("Invalid argument -> " + agreement + ", please try again!")

    # download the video and progress bar
    print("Downloading video [ "+yt_title+" ]...:")
    my_video.download(output_path=path)
    print("Your video is downloaded succesfully!")
    
#-------FUNCTION CALLS-------------------------------------------
if str(download_type)=="a":
    download_audio(url,download_location)

elif str(download_type)=="v":
    download_video(url,download_location)

else:
    print("Invalid argument -> "+download_type+", please try again!")