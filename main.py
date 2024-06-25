import gradio as gr
from pytube import YouTube
from pathlib import Path
import os

def download_links(urls, dir_path, type):
    urls=urls.split("\n")
    for i in range (len(urls)):
        if(type=='video'):
            try:
                yt =YouTube(urls[i])
                video = yt.streams.get_highest_resolution()
                video.download(filename=f"{video.title}.mp4", output_path=dir_path)
                # return("The video "+str(i)+" is downloaded in MP4")
            except KeyError:
                return("Unable to fetch video information. Please check the video URL or your network connection.")
        else:
            try:
                video = YouTube(urls[i])
                stream = video.streams.filter(only_audio=True).first()
                stream.download(filename=f"{video.title}.mp3", output_path=dir_path)
                # return("The video "+str(i)+" is downloaded in MP3")
            except KeyError:
                return("Unable to fetch video information. Please check the video URL or your network connection.")

def download(link_audio, link_video, dir_video, dir_audio):
    if(dir_video==""):
        return("Please insert the directory path")

    else:
        if(link_audio=="" and link_video==""):
            return("Please insert at least one link", )
        if(link_audio!=""):
            download_links(link_audio, dir_audio, 'audio')
        if(link_video!=""):
            download_links(link_video, dir_video, 'video')
        return("All done")
    

if __name__=='__main__':

    with gr.Blocks() as demo:

        gr.Markdown("# Youtube video downloader")
        with gr.Row():
            link_audio=gr.TextArea(label="Download mp3")
            link_video=gr.TextArea(label="Download mp4")
        with gr.Row():
            dir_audio=gr.Textbox(label="Directory path:")
            dir_video=gr.Textbox(label="Directory path:")
        b_download=gr.Button("Download")
        with gr.Row():
            result=gr.Textbox("", label="Result: ")
            # result_video=gr.Textbox("", label="Result video: ")

        b_download.click(fn=download, inputs=[link_audio, link_video, dir_audio, dir_video], outputs=[result])


    demo.launch(share=False)



