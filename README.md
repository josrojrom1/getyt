# getyt v2.0
Welcome to getyt project!

Hi im tric0, and getyt is a tool designed in Python to learn how to work with Youtube streams, only for legal purposes.

        INDEX

    1 - Installation guide
    2 - Python libraries
    3 - Avaible functions


1 - INSTALLATION GUIDE

    If you want to install it make sure to follow the instructions below to make it work.

    Install Python and virtual environment for install all the dependencies:
    - sudo pacman -S python python-virtualenv

    Clone the repository from GitHub in the actual route:
    - git clone https://github.com/tric0ma/getyt.git

    Change directory and go inside the new folder called "getyt":
    - cd getyt

    Activate virtual environment:
    - source venv_getyt/Scripts/activate

    Install python libraries if you dont have them:
    - pip install pytube
    - pip install tk

    Run the python script. You have to be in getyt directory:
    - python getyt.py

2 - PYTHON LIBRARIES
    In this project we are using the next modules:

    - os
    - pytube (YouTube)
    - tkinter (Tk, Label, Button, Entry, PhotoImage, RIDGE, filedialog)

3 - AVAIBLE FUNCTIONS
    In the actual version of getyt you can use the following functions:

    - GUI for getyt with tkinter
    - Check if URL is valid
    - Error logs
    - Download audio from YouTube URL
    - Download highest resolution video from Youtube URL
    - Download folder path selection
    - Try to bypass age restricted video