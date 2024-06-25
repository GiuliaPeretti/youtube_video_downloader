import gradio as gr
from pytube import YouTube
import os

def download(url, type):
    print(type)
    if (len(type)!=1):
        return("Please choose one type")
    elif(type[0]=='video'):
        yt =YouTube(url)
        # video = yt.streams.filter(only_audio=True).first() 
        video = yt.streams.get_highest_resolution()
        video.download(filename=f"{video.title}.mp3")
        return("video")
    else:
        try:
            video = YouTube(url)
            stream = video.streams.filter(only_audio=True).first()
            stream.download(filename=f"{video.title}.mp3")
            return("The video is downloaded in MP3")
        except KeyError:
            return("Unable to fetch video information. Please check the video URL or your network connection.")

if __name__=='__main__':

    with gr.Blocks() as demo:

        gr.Markdown("# Youtube video downloader")
        type=gr.CheckboxGroup(label="Audio:", choices=['audio', 'video'])
        link=gr.Textbox(label="Link:")
        b_download=gr.Button("Download")
        result=gr.Textbox("")

        b_download.click(fn=download, inputs=[link, type], outputs=[result])


    demo.launch(share=False)



