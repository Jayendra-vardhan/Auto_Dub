#Pytube   
from pytube import YouTube
import os
import sys
def download_video(link_user):
# url input from user
    yt = YouTube(link_user)
    print(yt.title)

    # extract only audio
    video = yt.streams.filter(only_audio=True).first()
    # check for destination to save file
    destination = "C:/Users/Bipul/OneDrive/Desktop/autodub_backend"
    # download the file
    out_file = video.download(output_path=destination)
    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    print("g")

    # result of success
    print(yt.title + " has been successfully downloaded.")
    return "Download done"