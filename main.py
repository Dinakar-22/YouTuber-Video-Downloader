from io import BytesIO
from pathlib import Path
from PIL import Image
import streamlit as st
from datetime import timedelta
from pytube import YouTube

icon = Image.open("yt-downloader.png")

st.set_page_config(
    page_icon=icon,
    page_title=" YouTuber Video Downloader ",
    layout="centered"
)

st.markdown(f"""
            <style>
            .stApp {{background-image: url("https://images.unsplash.com/photo-1523821741446-edb2b68bb7a0?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"); 
                     background-attachment: fixed;
                     background-size: cover}}
         </style>
         """, unsafe_allow_html=True)


c30, c31, c32 = st.columns([0.2, 0.09, 3.2])

with c30:

    st.caption("")

    st.image("yt-downloader.png", width=60)

with c32:

    st.title("YouTuber Video Downloader")


st.subheader(' ', divider='rainbow')

@st.cache_data(show_spinner=False)
def download_video(url):
    buffer = BytesIO()
    youtube_video = YouTube(url)
    video = youtube_video.streams.get_highest_resolution()
    default_filename = video.default_filename
    return default_filename, buffer

def main():
    url = st.text_input("Insert Youtube URL:")
    size = len(url)
    if size <= 0:
        st.write("Please Enter the URL...")
    else :
        yt_video = YouTube(url)

        image_yt = yt_video.thumbnail_url
        time_length   = (str(timedelta(seconds=yt_video.length)))
        if url:
            with st.spinner("Downloading Video Stream from Youtube..."):
                default_filename, buffer = download_video(url)
            st.write("Title: ",yt_video.title)
            st.write(f'Time Length: `{time_length}` seconds')
            st.image(image_yt, caption="Thumbnail")
            title_vid = Path(default_filename).with_suffix(".mp3").name
            st.download_button(
                label="Download video",
                data=buffer,
                file_name=title_vid,
            )
    
if __name__ == "__main__":
    main()
