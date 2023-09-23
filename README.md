# getyt
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
    - source entornovirtual/bin/activate

    Install python libraries if you dont have them:
    - pip install pytube pytube.cli

    Run the python script. You have to be in getyt directory:
    - python getyt.py

2 - PYTHON LIBRARIES
    In this project we are using the next dependencies:

    - pytube
    - pytube.cli
    - os
    - time

3 - AVAIBLE FUNCTIONS
    In the actual version of getyt you can use the following functions:

    - Download audio from YouTube URL
    - Download video in the highest resolution
    - Oauth anc oauth_cache for bypassing age restricted videos (using youtube account)


