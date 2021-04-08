from tkinter import *
from pytube import YouTube
import tkinter.messagebox
#"https://www.youtube.com/watch?v=ET9zvLo87mY"
def download_the_youtube():
    
       
    yt = YouTube(number1.get())
    dw  = yt.streams.get_by_itag(18)
#"D:/"
    dw.download(number2.get())
    var = "successfully downloaded"
    tkinter.messagebox.showinfo("you tube video downloader.",  "successfully installed")
 
 
root = Tk()
 
 
root.title("You tube video downloader")
root.iconbitmap('favicon.ico')
root.geometry('350x200')
 
 
 
lbl = Label(root, text = "Enter the youtube-link")
lbl.grid(column =0, row =0)
lb2 = Label(root, text = "Enter the path (D:/ or C:/)")
lb2.grid(column =0, row =1)
number1 = StringVar()
number2 = StringVar()
 
txt = Entry(root, textvariable = number1, width=70)

txt.grid(column =28, row =0)
yxt = Entry(root, textvariable = number2, width=70)
yxt.grid(column =28, row =1)
 
 
 
 
 
 
btn = Button(root, text = "download the video" ,
             fg = "red", command=download_the_youtube)
 
btn.grid(column=28, row=3)
photo = PhotoImage(file = r"hello.png")
label = Label(image= photo)
#label.image =  photo
label.grid(row=4 , column=28)
root.mainloop()