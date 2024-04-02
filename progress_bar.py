from pytube import YouTube
import tkinter as tk
from tkinter import ttk
import sys
import time

root = tk.Tk()
root.title("Progress Bar")
root.minsize(500, 500)
def progress_func(stream, chunk, bytes_remaining):
    current = stream.filesize - bytes_remaining
    percent_done = int(100 * current / stream.filesize)
    if percent_done > 50 and percent_done < 60:
        progress_bar['value'] += 50
        print(percent_done)
        text.set(f"Download in Progress...\n{percent_done}%")
        root.update_idletasks()
    if percent_done > 99:
        time.sleep(1)
        print(percent_done)
        progress_bar['value'] += 49.9
        text.set("Download Completed!")

def bytes_to_megabytes(bytes_size):
    megabytes_size = bytes_size / (1024 ** 2)
    return megabytes_size

def download_video():
    video.get_highest_resolution().download()

#def completed_download():
#    progress_bar.stop()
#    print('Download Completed')


yt = YouTube("https://www.youtube.com/watch?v=7dZmeh_28Eo&ab_channel=BusinessInsider",
#yt = YouTube("https://www.youtube.com/watch?v=OTkq4OsG_Yc",
             on_progress_callback=progress_func
             )
video = yt.streams.filter(progressive=True)

progress_bar = ttk.Progressbar(root, orient='horizontal', length=300, mode='determinate')
progress_bar.pack(padx=10, pady=20)

finish = tk.Label(root, foreground='Green')
finish.pack(padx=20, pady=20)

text = tk.StringVar()
finish['textvariable'] = text
text.set(f"\n")

start_button = ttk.Button(root, text='Start', command=download_video)
start_button.pack(padx=10, pady=10)

#stop_button = ttk.Button(root, text='Stop', command=completed_download)
#stop_button.pack(padx=10, pady=10)


'''
def progress_func(stream, chunk, bytes_remaining):
    current = stream.filesize - bytes_remaining
    done = int(50 * current / stream.filesize)

    sys.stdout.write(
        "\r[{}{}] {} MB / {} MB".format(
                                        '=' * done,
                                         ' ' * (50 - done),
                                        "{:.2f}".format(bytes_to_megabytes(current)),
                                        "{:.2f}".format(bytes_to_megabytes(stream.filesize))
                                        )
                    )
                    
    sys.stdout.flush()

def bytes_to_megabytes(bytes_size):
    megabytes_size = bytes_size / (1024 ** 2)
    return megabytes_size
    
yt = YouTube(youtube_link, on_progress_callback=progress_func)
'''

root.mainloop()