## getyt v3.1.1

![getyt_image_1](https://github.com/josrojrom1/getyt/assets/32680720/6599320f-5adf-49fe-8063-786edd7d3416)

**getyt** is a tool designed in Python which works for Linux and Windows, to learn how to work with Youtube **streams**, only for **legal purposes**. The project uses the pytube and tkinter modules.

# Installing
Make sure you are inside the repository folder.
### Virtual environment
It is recommended to use a virtual environment, where 'name' is the name you want, without quotes.
```
python -m venv 'name'
```
Activate the virtual environment where 'name' is the name from the previous step.
```
source name/bin/activate
```
### Installing dependencies
Use the `pip install -r` command to install the dependencies of the "requirements.txt" document.
```
pip install -r requirements.txt
```
# Using getyt
To run the script simply use `sudo` (make sure you are in a virtual environment):
```
sudo python getyt.py
```
It will request an **URL**, for example: *https://www.youtube.com/watch?v=eTOKXCEwo_8&ab_channel=ThePirateBayAwayFromKeyboard*

![getyt_image_2](https://github.com/josrojrom1/getyt/assets/32680720/4a1cfa40-13fd-4506-806b-9b9bb32f3325) ![getyt_image_5](https://github.com/josrojrom1/getyt/assets/32680720/c1a007d9-3a3f-4277-8e98-370574162552)

The tool **checks** if the URL is valid or not, showing the corresponging log. If the URL is valid, the user will be able to **download** the highest quality **video** or **audio** stream. After clicking it will show the percentage of download and the megabytes downloaded with respect to the total megabytes.

![getyt_image_3](https://github.com/josrojrom1/getyt/assets/32680720/5203dfb1-0d25-4fb1-9874-dcdb79468ca6) ![getyt_image_4](https://github.com/josrojrom1/getyt/assets/32680720/0e4a3cd4-c7e2-4ea1-abd2-382529e117e0)

Remember to use the `deactivate` command when you finish using the getyt tool to exit virtual environment.

# Available functions
In the actual version of getyt you can use the following functions:

- GUI for getyt designed with tkinter
- Check if URL is valid
- Error logs
- Download audio from YouTube URL
- Download highest resolution video from Youtube URL
- Select download path folder
- Bypass age restricted videos (most of links)
- Download private and hidden links
- Red log when try to download some rare links

<br/>
<br/>

---

*by José Joaquín Rojas Romero aka tric0 - josrojrom1@alum.us.es*



