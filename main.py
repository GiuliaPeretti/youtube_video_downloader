import gradio as gr
from pytube import YouTube
import os

def download(link):
    print(link)
    link=str(link)
    yt =YouTube(str(link))
    video = yt.streams.filter(only_audio=True).first() 
    video.download()
    out_file = video.download(output_path="C:\\Users\\giuli\\Documents\\GitHub\\youtube_video_downloader\\video\\") 
  
    # save the file 
    base, ext = os.path.splitext(out_file) 
    new_file = base + '.mp3'
    os.rename(out_file, new_file) 
    print(out_file)
    os.remove(out_file)

    return("Fatto")

if __name__=='__main__':

    with gr.Blocks() as demo:

        gr.Markdown("# Youtube video downloader")
        audio_type=gr.CheckboxGroup(label="Audio:", choices=['mp3'])
        video_type=gr.CheckboxGroup(label="Video:", choices=['mp4'])
        link=gr.Textbox(label="Link:")
        b_download=gr.Button("Download")
        result=gr.Textbox("")

        b_download.click(fn=download, inputs=[link], outputs=[result])


    demo.launch(share=False)



