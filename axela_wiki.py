#import sv_ttk
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo, askyesno
from tkinter import WORD
import wikipedia

def axelaprocess():
   cmd  = text.get()
   cmd = cmd.lower()
   if "get" in cmd:
       if "from" in cmd:
           if "wikipedia" in cmd:
                cmd = cmd.replace("wikipedia", "")
                cmd = cmd.replace("get", "")
                cmd = cmd.replace("from", "")
                results = wikipedia.summary(cmd, sentences=3, auto_suggest=False)
                showinfo(
                    title='Results from Wikipedia',
                    message=results
                )
root = tk.Tk()
root.title('Axela Wikipedia Engine')
root.iconbitmap('axelaico.ico')
#sv_ttk.use_light_theme()
root.geometry("250x150")
text = tk.StringVar()
textbox = ttk.Entry(root, textvariable=text)
textbox.pack(expand=True)
login_button = ttk.Button(root, text="Ask Axela!", command=axelaprocess, style="Accent.TButton")
login_button.pack(expand=True)
textbox.focus()
# Pack it
root.mainloop() 
