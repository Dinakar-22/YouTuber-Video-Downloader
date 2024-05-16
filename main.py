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

def main():

    url = st.text_input("Enter the url :")
    yt = YouTube(url)
    time_length   = (str(timedelta(seconds=yt.length)))
    size = len(url)

    if size <= 0:
        st.write("Please Enter the URL...")
        
    else:

        vidoe = yt.streams.get_highest_resolution()
        st.subheader(f'Title : {yt.title} ')
        st.write(f'Time Duraction : `{time_length}`')
        yt_thumbnail = yt.thumbnail_url
        st.image(yt_thumbnail, caption="`Video Thumbnail`")

        if st.button("Download"):
            try:
                vidoe.download()
            except Exception:
                st.write("Error Occured while downloading vidoe please try again")
            st.write("Download Completed Successfully")

if __name__ == "__main__" :
    main()
