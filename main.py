import streamlit as st
from pytube import YouTube
from PIL import Image

icon = Image.open("yt-downloader.png")

st.set_page_config(
    page_icon=icon,
    page_title=" 💻 YouTuber Video Downloader ⬇️",
    layout= "wide"
)

st.header(" 💻 YouTuber Video Downloader ⬇️")
st.subheader(' ', divider='rainbow')

try:
    
    video_link = st.text_input("Enter the YouTube Video Url:")

    yt = YouTube(video_link)

    image_yt = yt.thumbnail_url
    time = yt.length
    st.write("Title: ",yt.title)
    st.write("Video Length: ", time)
    st.image(image_yt, caption="Thumbnail")
    

    dowload = yt.streams.get_highest_resolution()

    if st.button("Download"):
        
        dowload.download()
        

except Exception:

    st.write("Error Please Try Again...")


rimaryColor="#F63366"
backgroundColor="#000000"
secondaryBackgroundColor="#C4CAD0"
textColor="#FCF7FF"
font="Press Start 2P"        