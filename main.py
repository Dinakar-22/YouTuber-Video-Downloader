import streamlit as st
from pytube import YouTube
from PIL import Image
import os 
from datetime import timedelta

icon = Image.open("yt-downloader.png")

st.set_page_config(
    page_icon=icon,
    page_title=" YouTuber Video Downloader ",
    layout="centered"
)

"""directory= '/Downloads'
if not os.path.exists(directory):
    os.makedirs(directory)"""

c30, c31, c32 = st.columns([0.2, 0.09, 3.2])

with c30:

    st.caption("")

    st.image("yt-downloader.png", width=60)

with c32:

    st.title("YouTuber Video Downloader")


st.subheader(' ', divider='rainbow')

try :
    
    video_link = st.text_input("Enter the YouTube Video Url:")

    yt = YouTube(video_link)

    file_name = yt.title
    time_length   = (str(timedelta(seconds=yt.length)))
    image_yt = yt.thumbnail_url

    st.subheader(f'Title: {yt.title}\nLength: `{time_length}` seconds')
    st.image(image_yt, caption="Thumbnail")
    

    dowload = yt.streams.get_highest_resolution()

    if st.button:
        dowload.download(filename= file_name)
        st.success('Download Complete', icon="✅")       
        st.balloons()
        
        
except Exception : 

    if len(video_link) < 0 :
        st.write("Enter Video Url !")
    else:
        st.write("Error Please Try Again...")


rimaryColor="#F63366"
backgroundColor="#000000"
secondaryBackgroundColor="#C4CAD0"
textColor="#FCF7FF"
font="Press Start 2P"        
