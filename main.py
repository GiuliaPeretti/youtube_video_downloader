import gradio as gr
from pytube import YouTube
from pathlib import Path
import tkinter as tk


class Downloader:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Youtube video downloader")
        self.root.geometry('400x400')


        self.up = tk.Frame(self.root)
        self.col1 = tk.Frame(self.up)
        self.col2 = tk.Frame(self.up)
        

        element_width=10


        self.mp3_label=tk.Label(self.col1, text='Links mp3: ')
        self.mp3_label.config(width=element_width)
        self.mp3_label.pack(padx=10, pady=10, fill="x")

        self.mp3_text=tk.Text(self.col1, height=10, width=20)
        self.mp3_text.pack(padx=10, pady=10, fill="both")

        self.mp3_path_label=tk.Label(self.col1, text='Path: ')
        self.mp3_path_label.pack(padx=10, pady=10, fill="x")

        self.mp3_path=tk.Entry(self.col1)
        self.mp3_path.pack(padx=10, pady=10, fill="x")





        self.mp4_label=tk.Label(self.col2, text='Links mp4: ')
        self.mp4_label.config(width=element_width)
        self.mp4_label.pack(padx=10, pady=10, fill="x")

        self.mp4_text=tk.Text(self.col2, height=10, width=20)
        self.mp4_text.pack(padx=10, pady=10, fill="both")

        self.mp4_path_label=tk.Label(self.col2, text='Path: ')
        self.mp4_path_label.pack(padx=10, pady=10, fill="x")

        self.mp4_path=tk.Entry(self.col2)
        self.mp4_path.pack(padx=10, pady=10, fill="x")

        self.col1.pack(expand=True, fill="both", side="left")
        self.col2.pack(expand=True, fill="both", side="right")
        self.up.pack(expand=True, fill="both", side="top")

        self.convert_button=tk.Button(self.root, text='Download', width=51, command=self.download_links)
        self.convert_button.pack(expand=True, fill="both", side="bottom")

        self.root.mainloop()

    def download_links(self):
        mp3_link=self.mp3_text.get()
        mp4_link=self.mp4_text.get()
        if mp3_link!='' and mp4_link!='':
            self.mp3_text.delete(0, 'end')
            self.mp3_text.insert(0, "Please insert at least one link")
            self.mp4_text.delete(0, 'end')
            self.mp4_text.insert(0, "Please insert at least one link")
        else:
            if mp3_link!='':
                mp3_link=mp3_link.split("\n")
                dir_path=self.mp3_path.get()
                for i in range(1,len(mp3_link)+1):
                    try:
                        video = YouTube(mp3_link[i-1])
                        stream = video.streams.filter(only_audio=True).first()
                        stream.download(filename=f"{video.title}.mp3", output_path=dir_path)
                    except KeyError:
                        self.mp3_text.delete(0, 'end')
                        self.mp3_text.insert(0, "Unable to fetch video "+i+" information. Please check the video URL or your network connection.")
                self.mp3_text.delete(0, 'end')
                self.mp3_text.insert(0, "Done")

            if mp4_link!='':
                mp4_link=mp4_link.split("\n")
                dir_path=self.mp4_path.get()
                for i in range(1,len(mp4_link)+1):
                    try:
                        video = YouTube(mp4_link[i-1])
                        stream = video.streams.filter(only_audio=True).first()
                        stream.download(filename=f"{video.title}.mp4", output_path=dir_path)
                    except KeyError:
                        self.mp4_text.delete(0, 'end')
                        self.mp4_text.insert(0, "Unable to fetch video "+i+" information. Please check the video URL or your network connection.")
                self.mp3_text.delete(0, 'end')
                self.mp3_text.insert(0, "Done")



        # urls=urls.split("\n")
        # for i in range (len(urls)):
        #     if(type=='video'):
        #         try:
        #             yt =YouTube(urls[i])
        #             video = yt.streams.get_highest_resolution()
        #             video.download(filename=f"{video.title}.mp4", output_path=dir_path)
        #             # return("The video "+str(i)+" is downloaded in MP4")
        #         except KeyError:
        #             return("Unable to fetch video information. Please check the video URL or your network connection.")
        #     else:
        #         try:
        #             video = YouTube(urls[i])
        #             stream = video.streams.filter(only_audio=True).first()
        #             stream.download(filename=f"{video.title}.mp3", output_path=dir_path)
        #             # return("The video "+str(i)+" is downloaded in MP3")
        #         except KeyError:
        #             return("Unable to fetch video information. Please check the video URL or your network connection.")

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
    Downloader()





# if __name__=='__main__':

#     with gr.Blocks() as demo:

#         gr.Markdown("# Youtube video downloader")
#         with gr.Row():
#             link_audio=gr.TextArea(label="Download mp3")
#             link_video=gr.TextArea(label="Download mp4")
#         with gr.Row():
#             dir_audio=gr.Textbox(label="Directory path:")
#             dir_video=gr.Textbox(label="Directory path:")
#         b_download=gr.Button("Download")
#         with gr.Row():
#             result=gr.Textbox("", label="Result: ")
#             # result_video=gr.Textbox("", label="Result video: ")

#         b_download.click(fn=download, inputs=[link_audio, link_video, dir_audio, dir_video], outputs=[result])


#     demo.launch(share=False)



