import gradio as gr
from pytube import YouTube
from pathlib import Path
import tkinter as tk
from customtkinter import *
import multiprocessing as mp


PINK='#ff70c8'
GREEN='#5ee0aa'
BLACK='#000000'

class Downloader:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Youtube video downloader")
        self.root.geometry('600x400')


        self.up = tk.Frame(self.root)
        self.col1 = tk.Frame(self.up)
        self.col2 = tk.Frame(self.up)
        

        self.mp3_label=CTkLabel(self.col1, text='Links mp3: ')
        self.mp3_label.pack(padx=10, pady=10, fill="x")

        self.mp3_text=CTkTextbox(self.col1, border_width=2, border_color=PINK, scrollbar_button_color=GREEN)
        self.mp3_text.pack(padx=10, pady=10, fill="both")

        self.mp3_path=CTkEntry(self.col1, placeholder_text='Directory path', border_width=2, border_color=PINK)
        self.mp3_path.pack(padx=10, pady=10, fill="x")


        self.mp4_label=CTkLabel(self.col2, text='Links mp4: ')
        self.mp4_label.pack(padx=10, pady=10, fill="x")

        self.mp4_text=CTkTextbox(self.col2, border_width=2, border_color=PINK, scrollbar_button_color=GREEN)
        self.mp4_text.pack(padx=10, pady=10, fill="both")

        self.mp4_path=CTkEntry(self.col2, placeholder_text='Directory path', border_width=2, border_color=PINK)
        self.mp4_path.pack(padx=10, pady=10, fill="x")


        self.col1.pack(expand=True, fill="both", side="left")
        self.col2.pack(expand=True, fill="both", side="right")
        self.up.pack(expand=True, fill="both", side="top")

        self.convert_button=CTkButton(self.root, text='Download',corner_radius=32,text_color=BLACK , fg_color=PINK, hover_color=GREEN, width=51, command=self.download_links)
        self.convert_button.pack(padx=10, pady=10,expand=True, fill="both", side="bottom")

        self.root.mainloop()

    def download_links(self):
        mp3_link=self.mp3_text.get("1.0",'end')
        mp4_link=self.mp4_text.get("1.0",'end')

        if mp3_link=='' and mp4_link=='':
            self.mp3_text.delete('1.0', 'end')
            self.mp3_text.insert('1.0', "Please insert at least one link")
            self.mp4_text.delete('1.0', 'end')
            self.mp4_text.insert('1.0', "Please insert at least one link")
        else:
            if mp3_link!='':
                mp3_link=mp3_link.split("\n")
                mp3_link.remove('')
                dir_path=self.mp3_path.get()
                if dir_path=='' and len(mp3_link)>0 and mp3_link[0]!='':
                    self.mp3_path.delete(0, 'end')
                    self.mp3_path.insert(0, 'Please insert a direcory path')
                elif mp3_link[0]!='':
                    # global mp3_results
                    # p=[]
                    # 
                    #     p.append(mp.Process(target=download, args=(mp3_link[i], dir_path, mp3_results, 'mp3', True, i)))
                    #     mp3_results.append('')
                    #     p[i].start()
                    # s=''
                    # for i in range(0,len(mp3_link)):
                    #     p[i].join()
                    #     s=s+mp3_results[i]
                    # print(s)
                    # self.mp3_text.delete('1.0', 'end')
                    # self.mp3_text.insert('1.0', s)
                    self.mp3_text.delete('1.0', 'end')
                    for i in range(1,len(mp3_link)+1):
                        try:
                            video = YouTube(mp3_link[i-1])
                            stream = video.streams.filter(only_audio=True).first()
                            stream.download(filename=f"{video.title}.mp3", output_path=dir_path)
                        except:
                            self.mp3_text.insert('1.0', "Unable to fetch video "+str(i)+" information. Please check the video URL or your network connection. \n")
                    self.mp3_text.insert('end', "Done")

            if mp4_link!='':
                mp4_link=mp4_link.split("\n")
                mp4_link.remove('')
                dir_path=self.mp4_path.get()
                if dir_path=='' and len(mp4_link)>0 and mp4_link[0]!='':
                    self.mp4_path.delete(0, 'end')
                    self.mp4_path.insert(0, 'Please insert a direcory path')
                elif mp4_link[0]!='':
                    self.mp4_text.delete('1.0', 'end')
                    for i in range(1,len(mp4_link)+1):
                        if (mp4_link[i-1]!=''):
                            try:
                                video = YouTube(mp4_link[i-1])
                                stream = video.streams.filter(only_audio=True).first()
                                stream.download(filename=f"{video.title}.mp4", output_path=dir_path)
                            except:
                                self.mp4_text.insert('1.0', "Unable to fetch video "+str(i)+" information. Please check the video URL or your network connection. \n")
                    if (len(mp4_link)>0 and mp4_link[0]!=''):
                        self.mp4_text.insert('end', "Done")

# def download(url, dir, mp3_results, e, only_audio, pos):
#     try:
#         video = YouTube(url)
#         stream = video.streams.filter(only_audio=only_audio).first()
#         stream.download(filename=f"{video.title}."+e, output_path=dir)
#         mp3_results[pos]="Done. \n"
#     except:
#         mp3_results[pos]="Unable to fetch video "+str(pos+1)+" information. Please check the video URL or your network connection. \n"


if __name__=='__main__':
    Downloader()
