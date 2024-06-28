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
from tkinter import RIDGE
from tkinter import filedialog
from tkinter import PhotoImage
from tkinter import messagebox
from pytube import YouTube
from pytube import exceptions
from pytube.innertube import InnerTube

class getyt:
    def __init__(self):
        ### URL INPUT LABEL ##########
        self.url_label = Label(root, text="Insert URL from YouTube")
        self.url_label.config(anchor="center", font=("Arial", 18), fg=font_color, background=background_color, padx=12, pady=12)
        self.url_label.grid(row=0, column=0)
        ### URL ENTRY ################
        self.url = Entry(root)
        self.url.config(width=40, font=("Arial", 14), fg=font_color, background=background_color, borderwidth=1)
        self.url.focus()
        self.url.grid(row=1, column=0, padx=12)
        ### CHECK BUTTON #############
        self.check_button = Button(root,text="Check URL", command=lambda: self.checkURL(getyt_instance.url.get()))
        self.check_button.config(anchor="center", padx=12, relief=RIDGE, fg=font_color, background=background_color)
        self.check_button.grid(row=3, column=0)
        ### DOWNLOAD LOCATION FOLDER ##
        if os.name == "nt":
            # Windows
            self.download_location = os.path.join(os.getenv("USERPROFILE"), "Downloads")
        else:  
            # Linux or macOS
            self.download_location = os.path.join(os.path.expanduser("~"), "Downloads")
        ### DOWNLOAD LOCATION #######
        self.download_location_label = Button(root, text="Download path: {}".format(self.download_location), command=self.on_click_download_location) 
        self.download_location_label.config(anchor="center", font=("Arial", 9), fg=font_color, background=background_color, padx=12, relief=RIDGE)
        self.download_location_label.grid(row=2, column=0)
        self.download_location_label.grid_configure(pady=12)
        ### SHORTED TITLE ############
        self.url_shorted_title = Label(root, text="")
        ### DOWNLOAD BUTTONS ########
        self.download_audio_btn = Button(root, text="Download Audio", command=lambda: self.download_stream(getyt_instance.url.get(), "audio", self.download_location))
        self.download_video_btn = Button(root, text="Download Video", command=lambda: self.download_stream(getyt_instance.url.get(), "video", self.download_location))
        ### SUCCESS/ERROR LOGS ##############
        self.url_ok = Label(root, text="URL OK! ✔")
        self.url_error = Label(root, text="Error: URL not valid, please try to use a valid one. \n")
        self.succes = Label(root, text="Download completed! ✔")
        self.succes.configure(background=background_color, fg="green", font=("Arial", 12))
        self.info = Label(root, text="(Copy and paste another URL for continue downloading)")
        self.info.configure(background=background_color, fg=font_color, font=("Arial", 9))
        self.cant_download_label = Label(root, text="Can't download this stream")
        self.cant_download_label.configure(anchor="center", font=("Arial", 9), fg="red", background=background_color, padx=12, pady=12)


    def on_click_download_location(self):
        self.new_download_location = filedialog.askdirectory()
        if str(self.new_download_location)=="":
            if os.name == "nt":
                # Windows
                self.new_download_location = os.path.join(os.getenv("USERPROFILE"), "Downloads")
            else:
                # Linux or macOS
                self.new_download_location = os.path.join(os.path.expanduser("~"), "Downloads")
        self.download_location = self.new_download_location
        self.download_location_label.config(text="Download path: {}".format(self.download_location))

    def checkURL(self,url):
        self.url_ok.grid_remove()
        self.url_error.grid_remove()
        self.succes.grid_remove()
        self.info.grid_remove()
        self.url.config(state="normal")
        self.download_video_btn.config(state="normal")
        self.download_audio_btn.config(state="normal")
        self.download_audio_btn.grid_remove()
        self.download_video_btn.grid_remove()
        self.url_shorted_title.grid_remove()
        self.cant_download_label.grid_remove()   
            
        try:
            ### URL INPUT ###############
            self.youtube = YouTube(url, use_oauth=False, allow_oauth_cache=False)
            self.yt_title= str(self.youtube.title)
            self.yt_title_short=str(self.youtube.title)[:36] + "..."
            self.url_title= Label(root, text=self.yt_title)
            self.url_shorted_title = Label(root, text=self.yt_title_short)
            self.url_title.config(anchor="center", background=background_color, fg=font_color, font=("Arial", 12), padx=12, pady=12)
            self.url_shorted_title.config(anchor="center", background=background_color, fg=font_color, font=("Arial", 12), padx=12, pady=12)
            self.url_shorted_title.grid(row=5, column=0)
            ### DOWNLOAD BUTTONS ########
            self.download_audio_btn.config(relief=RIDGE, fg=font_color, background=background_color)
            self.download_audio_btn.grid(row=6, column=0)
            self.download_video_btn.config(relief=RIDGE, fg=font_color, background=background_color)
            self.download_video_btn.grid(row=6, column=0)
            self.download_audio_btn.place(x=90,y=250)
            self.download_video_btn.place(x=225,y=250)
            ### OK LOG/GREEN CHECK ######
            self.url_ok.config(background=background_color, fg="green", font=("Arial", 9), pady=12, padx=12)
            self.url_ok.grid(row=4, column=0)
            #self.url_error.grid_remove()
                
        except Exception as e:

            ### INVALID URL INPUT #######
            self.url_error.config(fg="red" ,background=background_color, font=("Arial", 9), pady=12, padx=12)
            self.url_error.grid(row=4, column=0)
            self.download_video_btn.grid_remove()
            self.download_audio_btn.grid_remove()
            self.download_audio_btn.place_forget()
            self.download_video_btn.place_forget()
            self.url_ok.grid_remove()
    #################################################
    # CHECK IF FILE ALREADY EXISTS IN DOWNLOAD PATH #
    def check_if_path_exists(self, path, stream):
        if os.path.exists(path):
            count = 1
            while os.path.exists(path):
                new_filename = f"{self.filename} ({count})"
                path = os.path.join(self.download_location, new_filename)
                count += 1
            stream.download(output_path=path, filename=new_filename, max_retries=5)
        else:
            stream.download(output_path=path, max_retries=5)
    ##########################
    # DOWNLOAD MAIN FUNCTION #
    def download_stream(self, url, format, path):
        path = str(path)
        self.download_video_btn.config(state="disabled")
        self.download_audio_btn.config(state="disabled")
        self.download_audio_btn.grid_remove()
        self.download_video_btn.grid_remove()
        self.download_audio_btn.place_forget()
        self.download_video_btn.place_forget()
        self.url_ok.grid_remove()

        try:
            self.youtube = YouTube(url, on_progress_callback=self.on_progress_download,use_oauth=False, allow_oauth_cache=False)
            #self.youtube.bypass_age_gate()
            self.filename = self.youtube.title#.replace('\\', " ").replace(">", " ").replace('"', " ").replace("/", " ").replace("|", " ").replace(".", " ").replace("?", " ").replace("*", " ").replace("&", " ").replace(":", " ").replace("<", " ")

            # Refactorizar codigo    
            if format == "video":
                stream = self.youtube.streams.get_highest_resolution()
                self.filename = "(video) "+self.filename
                
            elif format=="audio":
                stream = self.youtube.streams.get_audio_only()
                self.filename = "(audio) "+self.filename

            if not path:    
                path = self.download_location
            path = os.path.join(path, self.filename) 
            self.check_if_path_exists(path, stream)
                
        except Exception as e:
            self.cant_download_label.configure(text=str(e))
            self.cant_download_label.grid(row=9, column=0)
            #print(str(e))
            #print("-> Error: " + str(e))

    #def abort_downloading(self, stream):
    #    stream.stop_download()
    #    download_label = Label(root, text="Download cancelled")

    def on_progress_download(self, stream, chunk, bytes_remaining):
        self.is_cancelled=False

        self.download_location_label.config(state="disabled")
        self.check_button.config(state="disabled")
        self.url.config(state="disabled")
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage_of_completion = round(bytes_downloaded / total_size * 100, 2)
        string_percentage = f"Downloading:  {percentage_of_completion} %   ( {bytes_downloaded/(1024*1024)} / {int(total_size/(1024*1024))} ) Mb"
        self.download_label = Label(root, text=string_percentage)
        self.download_label.config(fg=font_color, background=background_color, font=("Arial", 9), pady=25)
        self.download_label.grid(row=8, column=0)

        #self.cancel_btn = Button(root,text="Cancel", command=lambda: self.abort_downloading(stream))
        #self.cancel_btn.grid(row=9, column=0)
            

        root.update()
        self.download_label.grid_remove()
            
        if percentage_of_completion == 100 :

            self.download_location_label.config(state="normal")
            self.url_error.grid_remove()
            self.url_shorted_title.grid_remove()
            self.check_button.config(state="normal")
            self.url.config(state="normal")
            self.succes.grid(row=5, column=0)
            self.succes.grid_configure(pady=12)
            self.info.grid(row=6, column=0)
            self.info.grid_configure(pady=12) 

if __name__ == '__main__':

    ### COLOR SCHEMA ############
    background_color = "#313338"
    font_color = "#FFFFFF"
    ### MAIN FRAME SETTINGS #####
    root = Tk()
    root.resizable(False, False)
    root.geometry("470x345")
    root.config(bg=background_color)
    root.title("YouTube Downloader")
    icon = PhotoImage(file="icon.png")
    root.iconphoto(True, icon)
    ### GETYT CLASS INSTANCE ####
    getyt_instance = getyt()
    ### MAIN LOOP ###############
    root.mainloop()