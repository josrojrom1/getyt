# getyt v3.1.0
Welcome to getyt project!

Hi im tric0, and getyt is a tool designed in Python to learn how to work with Youtube streams, only for legal purposes.

                                                      INDEX
                                                
                                                  1 - Installation guide
                                                    1.1 - Windows
                                                    1.2 - Linux
                                                  2 - Python libraries
                                                  3 - Avaible functions


1 - INSTALLATION GUIDE

    If you want to install it make sure to follow the instructions below to make it work.
    
   1.1 -  Installation process on WINDOWS:

            Clone the repository or download the ZIP code. Run getyt.exe.
    
   1.2 -  Installation process on LINUX: 

            Clone the repository from GitHub in the actual route:
            - git clone https://github.com/tric0ma/getyt.git
        
            Change directory and go inside the new folder called "getyt":
            - cd getyt

            Create virtual environment:
            - python -m venv venv_getyt
            
            Activate virtual environment:
            - source venv_getyt/bin/activate (Linux)
            - source venv_getyt/Scripts/activate (Windows)
        
            Install the dependencies:
            - pip install -r requirements.txt 
                
            (optional) Install python libraries if you dont have requirements.txt:
            - pip install pytube
            - pip install tk
        
            Run the python script. You have to be in getyt directory:
            - python getyt.py

2 - PYTHON LIBRARIES

    In this project we are using the next modules:

    - os
    - pytube (YouTube)
    - tkinter (Tk, Label, Button, Entry, RIDGE, filedialog)

3 - AVAIBLE FUNCTIONS

    In the actual version of getyt you can use the following functions:

    - GUI for getyt designed with tkinter
    - Check if URL is valid
    - Error logs
    - Download audio from YouTube URL
    - Download highest resolution video from Youtube URL
    - Download folder path selector
    - Try to bypass age restricted video
