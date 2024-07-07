import gradio as gr
from pytube import YouTube
from pathlib import Path
import tkinter as tk
from customtkinter import *

PINK='#ff70c8'
GREEN='#5ee0aa'
BLACK='#000000'

#C:\Users\giuli\Downloads
class Downloader:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Youtube video downloader")
        self.root.geometry('600x400')


        self.up = tk.Frame(self.root)
        self.col1 = tk.Frame(self.up)
        self.col2 = tk.Frame(self.up)
        

        element_width=10


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

        print(mp3_link)
        print(mp4_link)

        if mp3_link=='' and mp4_link=='':
            self.mp3_text.delete('1.0', 'end')
            self.mp3_text.insert('1.0', "Please insert at least one link")
            self.mp4_text.delete('1.0', 'end')
            self.mp4_text.insert('1.0', "Please insert at least one link")
        else:
            if mp3_link!='':
                mp3_link=mp3_link.split("\n")
                mp3_link.remove('')
                print(mp3_link)
                dir_path=self.mp3_path.get()
                if dir_path=='' and len(mp3_link)>0 and mp3_link[0]!='':
                    self.mp3_path.delete(0, 'end')
                    self.mp3_path.insert(0, 'Please insert a direcory path')
                self.mp3_text.delete('1.0', 'end')
                for i in range(1,len(mp3_link)+1):
                    print(mp3_link[i-1])
                    try:
                        video = YouTube(mp3_link[i-1])
                        stream = video.streams.filter(only_audio=True).first()
                        stream.download(filename=f"{video.title}.mp3", output_path=dir_path)
                    except:
                        self.mp3_text.insert('1.0', "Unable to fetch video "+str(i)+" information. Please check the video URL or your network connection. \n")
                if len(mp3_link)>0 and mp3_link[0]!='':
                    self.mp3_text.insert('end', "Done")

            if mp4_link!='':
                print('mp4_link: '+str(mp4_link))
                mp4_link=mp4_link.split("\n")
                mp4_link.remove('')
                print(mp4_link)
                dir_path=self.mp4_path.get()
                if dir_path=='' and len(mp4_link)>0 and mp4_link[0]!='':
                    self.mp4_path.delete(0, 'end')
                    self.mp4_path.insert(0, 'Please insert a direcory path')
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



if __name__=='__main__':
    Downloader()
