import tkinter as tk
from tkinter import ttk
from pytube import YouTube
import time
from tkinter import filedialog as fd

# Window
root = tk.Tk()
root.title("Youtube Video Downloader", )
root.minsize(500, 500)

def progress_func(stream, chunk, bytes_remaining):
    current = stream.filesize - bytes_remaining
    percent_done = int(100 * current / stream.filesize)
    if percent_done > 50 and percent_done < 60:
        progress_bar['value'] += 50
        text.set(f"Download in Progress...\n{percent_done}%")
        root.update_idletasks()
    if percent_done > 99:
        time.sleep(0.5)
        progress_bar['value'] += 49.9
        text.set("Download Completed!")

def select_destination():
    global destination
    destination = fd.askdirectory()
    destination_text['text'] = destination

def confirm():
    youtube_link = type_link.get()
    video_type_final = video_choice[video_type.curselection()[0]]
    resolution_final = resolution['values'][resolution.current()]

    yt = YouTube(youtube_link, on_progress_callback=progress_func)

    if video_type_final == 'Progressive : Video and Audio in same file':
        video_filter = yt.streams.filter(progressive=True)
    elif video_type_final == 'Adaptive: Video and Audio separated':
        video_filter = yt.streams.filter(adaptive=True)
    elif video_type_final == 'MP4':
        video_filter = yt.streams.filter(file_extension='mp4')

    confirmed_video = video_filter.get_by_resolution(resolution_final)
    print(confirmed_video)

    download = yt.streams.get_by_itag(confirmed_video.itag)
    download.download(destination)

# GUI
entry_label = tk.Label(root, text="Insert the link of the video you want to download below!")
entry_label.pack(anchor='center', padx=10, pady=10)

type_link = tk.Entry(root, width=50)
type_link.pack(anchor='center', padx=10, pady=10)

# Options Frame
options_frame = tk.Frame(root)

resolution = ttk.Combobox(options_frame)
resolution['values'] = ['144p', '240p', '360p', '720p', '1080p']
resolution.pack(padx=10, pady=10)

video_choice = ['Progressive : Video and Audio in same file', 'Adaptive: Video and Audio separated', 'MP4']
video_choice_var = tk.StringVar(value=video_choice)
video_type = tk.Listbox(options_frame, listvariable=video_choice_var, height=len(video_choice), width=40)
video_type.pack(padx=10, pady=10)

options_frame.pack()

# Location to store video
choose_location = tk.Button(root, text="Choose Location to store video", width=30, command=select_destination)
choose_location.pack(padx=10, pady=10)
destination_text = tk.Label(root, text="Folder Destination", foreground='Green')
destination_text.pack(padx=10, pady=10)

#Download Progress Bar
progress_bar = ttk.Progressbar(root, orient='horizontal', length=300, mode='determinate')
progress_bar.pack(padx=10, pady=20)

finish = tk.Label(root, foreground='Green')
finish.pack(padx=20, pady=20)

text = tk.StringVar()
finish['textvariable'] = text
text.set(f"\n")

# Start Download
confirm_button = tk.Button(root, text='Click here to confirm selection', command=confirm)
confirm_button.pack(padx=10, pady=10)

root.mainloop()