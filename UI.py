import sys
import os
import tkinter
from tkinter.constants import *

def run():
    os.system('python new_M3.py')


tk = tkinter.Tk()
frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=2)
label = tkinter.Label(frame, text="Stock Market Forum Sentiment Analyzer")
label.pack(fill=X, expand=2)
#button = tkinter.Button(frame,text="Start Sentiment Analysis",command=tk.destroy)
button = tkinter.Button(frame,text="Start Sentiment Analysis",command=run)

button.pack(side=BOTTOM)
tk.mainloop()

