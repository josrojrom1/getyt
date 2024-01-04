# Copyright (c) 2024 José Joaquín Rojas Romero
#
# This program is a YouTube video downloader application written in 
# Python. It uses the tkinter library to create a simple GUI.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Python libraries used:

### IMPORTS #################       
import os
from tkinter import Tk
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import PhotoImage
from tkinter import RIDGE
from tkinter import filedialog
from pytube import YouTube

### COLOR SCHEMA ############
background_color = "#313338"
font_color = "#FFFFFF"

### MAIN FRAME SETTINGS #####
root = Tk()
root.resizable(False, False)
root.geometry("475x400")
root.config(bg=background_color)
root.title("YouTube Downloader")
icon = PhotoImage(file="icon.png")
root.iconphoto(True, icon)

if os.name == "nt":
    # Windows
        download_location = os.path.join(os.getenv("USERPROFILE"), "Downloads")

else:
    # Linux or macOS
        download_location =  os.path.join(os.path.expanduser("~"), "Downloads")
  
### DOWNLOAD FOLDER PATH ####
def get_downloads_folder_path():
    #global download_location

    download_location = filedialog.askdirectory()
    if download_location:
        download_location_label.config(text="Download path: {}".format(download_location))


### DOWNLOAD FUNCTION #######
def download(url, format, path):
    
    try:
        youtube = YouTube(url, on_progress_callback=on_progress_download,use_oauth=False, allow_oauth_cache=False)
        youtube.bypass_age_gate()
        filename = youtube.title.replace('\\', " ").replace(">", " ").replace('"', " ").replace("/", " ").replace("|", " ").replace(".", " ").replace("?", " ").replace("*", " ").replace("&", " ").replace(":", " ").replace("<", " ")
        
        if format == "video":
            stream = youtube.streams.get_highest_resolution()
            file_size = stream.filesize
            filename = "(video) "+filename
            if not path:
                path = get_downloads_folder_path()
                path = os.path.join(path, filename) 
            else:
                path = os.path.join(path, filename)
                stream.download(output_path=path)

        elif format=="audio":
            stream = youtube.streams.get_audio_only()
            file_size = stream.filesize

            filename = "(audio) "+filename
            if not path:
                path = get_downloads_folder_path()
                path = os.path.join(path, filename) 
            else:
                path = os.path.join(path, filename)
                stream.download(output_path=path)
        
    except Exception as e:
        print("Error: " + str(e))

### DOWNLOAD AUDIO FUNCTION #
def downloadAudio(url,path):
    format = "audio"
    get_downloads_folder_path()
    download(url, format, path)
    
### DOWNLOAD VIDEO FUNCTION #
def downloadVideo(url, path):
    format = "video"
    get_downloads_folder_path()
    download(url, format, path)
 
### PROGRESS % FUNCTION ###
def on_progress_download(stream, chunk, bytes_remaining):
    
    download_location_label.config(state="normal")
    download_video_btn.config(state="disabled")
    download_audio_btn.config(state="disabled")
    check_button.config(state="disabled")
    url_entry.config(state="disabled")

    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = round(bytes_downloaded / total_size * 100, 2)
    string_percentage = f"Downloading: {percentage_of_completion} %"
    download_label = Label(root, text=string_percentage)
    download_label.config(fg=font_color, background=background_color, font=("Arial", 9))
    download_label.grid(row=8, column=0)
    root.update()
    download_label.grid_remove()
    
    if percentage_of_completion == 100 :

        download_location_label.config(state="normal")
        url_error.grid_remove()
        url_shorted_title.grid_remove()
        download_video_btn.config(state="disabled")
        download_audio_btn.config(state="disabled")
        download_audio_btn.grid_remove()
        download_video_btn.grid_remove()
        check_button.config(state="normal")
        url_entry.config(state="normal")
        succes.grid(row=5, column=0)
        succes.grid_configure(pady=12)
        info.grid(row=6, column=0)
        info.grid_configure(pady=12)

### URL CHECK FUNCTION ######
def checkURL(url):
    global url_shorted_title
    url_error.grid_remove()
    succes.grid_remove()
    info.grid_remove()
    url_entry.config(state="normal")
    download_video_btn.config(state="normal")
    download_audio_btn.config(state="normal")
    download_audio_btn.grid_remove()
    download_video_btn.grid_remove()
    url_ok.grid_remove()
    #url_shorted_title.grid_remove()   
       

    

    try:
        youtube = YouTube(url, on_progress_callback=on_progress_download,use_oauth=False, allow_oauth_cache=False)
        yt_title= str(youtube.title)
        yt_title_short=str(youtube.title)[:36] + "..."
        url_title= Label(root, text=yt_title)
        url_shorted_title = Label(root, text=yt_title_short)
        url_title.config(anchor="center", background=background_color, fg=font_color, font=("Arial", 12), padx=12, pady=12)
        url_shorted_title.config(anchor="center", background=background_color, fg=font_color, font=("Arial", 12), padx=12, pady=12)
        url_shorted_title.grid(row=5, column=0)

                
        # BUTTON TO DOWNLOAD AUDIO  #   
        download_audio_btn.grid(row=6, column=0)

        # BUTTON TO DOWNLOAD VIDEO  #
        download_video_btn.grid(row=7, column=0)
        download_video_btn.grid_configure(pady=12)
        

        ### OK LOG/GREEN CHECK ######
        url_ok.grid(row=4, column=0)
        url_error.grid_remove()
        





    except Exception as e:

        ### INVALID URL INPUT #######
        url_error.grid(row=4, column=0)
        url_ok.grid_remove()
        
    if url_error.winfo_ismapped():
        download_video_btn.config(state="disabled")
        download_audio_btn.config(state="disabled")
    
### URL INPUT ###############
url_label = Label(root, text="Insert URL from YouTube")
url_label.config(anchor="center", font=("Arial", 18), fg=font_color, background=background_color, padx=12, pady=12)
url_label.grid(row=0, column=0)
url_entry = Entry(root, width=40, font=("Arial", 14), fg=font_color, background=background_color, borderwidth=1)
url_entry.focus()
url_entry.grid(row=1, column=0)
url_entry.grid_configure(padx=12)

### DOWNLOAD LOCATION #######
download_location_label = Button(root, text="Download path: {}".format(download_location), command=get_downloads_folder_path)
download_location_label.config(anchor="center", font=("Arial", 9), fg=font_color, background=background_color, padx=12, relief=RIDGE)
download_location_label.grid(row=2, column=0)
download_location_label.grid_configure(pady=12)
#download_location_label["border"]="0"

### URL CHECK ###############
check_button = Button(root,text="Check URL", command=lambda: checkURL(url_entry.get()))
check_button.config(anchor="center", padx=12, relief=RIDGE, fg=font_color, background=background_color)
check_button.grid(row=3, column=0)

### DOWNLOAD BUTTONS ########
download_audio_btn = Button(root, text="Download Audio", command=lambda: downloadAudio(url_entry.get(), download_location))
download_audio_btn.config(relief=RIDGE, fg=font_color, background=background_color, padx=12)
download_video_btn = Button(root, text="Download Video", command=lambda: downloadVideo(url_entry.get(), download_location))
download_video_btn.config(relief=RIDGE, fg=font_color, background=background_color, padx=12)


### SUCCESS/ERROR LOGS ######
url_ok = Label(root, text="URL OK! ✔")
url_ok.config(background=background_color, fg="green", font=("Arial", 9), pady=12, padx=12)
url_error = Label(root, text="Error: URL not valid, please try to use a valid one.")
url_error.config(fg="red" ,background=background_color, font=("Arial", 9), pady=12, padx=12)
succes = Label(root, text="Download completed! ✔")
succes.configure(background=background_color, fg="green", font=("Arial", 12))
info = Label(root, text="(Copy and paste another URL for continue downloading)")
info.configure(background=background_color, fg=font_color, font=("Arial", 9))


    

### MAIN LOOP ###############
root.mainloop()

# This program is freely available for anyone to use, but please use it responsibly.
# Please respect the copyright of others and don't misuse this code for illegal purposes.
# If you find this code useful, please consider sharing it with others.
# Let's make the world a better place with open-source software!