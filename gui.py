import tkinter as tk
from tkinter import ttk

# Window
root = tk.Tk()
root.title("Youtube Video Downloader", )
root.minsize(500, 500)

def confirm():
    video_type_final = video_choice[video_type.curselection()[0]]
    resolution_final = resolution['values'][resolution.current()]


entry_label = tk.Label(root, text="Insert the link of the video you want to download below!")
entry_label.pack(anchor='center', padx=10, pady=10)

type_link = tk.Entry(root, width=50)
type_link.pack(anchor='center', padx=10, pady=10)

# Options Frame
options_frame = tk.Frame(root)

video_choice = ['Progressive : Video and Audio in same file', 'Adaptive: Video and Audio separated', 'MP4']
video_choice_var = tk.StringVar(value=video_choice)
video_type = tk.Listbox(options_frame, listvariable=video_choice_var, height=len(video_choice), width=40)
video_type.pack(padx=10, pady=10)

resolution = ttk.Combobox(options_frame)
resolution['values'] = ['144p', '240p', '360p', '720p', '1080p']
resolution.pack(padx=10, pady=10)

options_frame.pack()

# Location to store video
choose_location = tk.Button(root, text="Choose Location to store video", width=30)
choose_location.pack(padx=10, pady=10)

confirm_button = tk.Button(root, text='Click here to confirm selection', command=confirm)
confirm_button.pack(padx=10, pady=10)









root.mainloop()