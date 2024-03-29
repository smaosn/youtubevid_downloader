from pytube import YouTube, Search

#yt = YouTube("https://www.youtube.com/watch?v=ZU2KtCDZjGM&ab_channel=KennethAcoustic")
yt = YouTube("https://www.youtube.com/watch?v=7dZmeh_28Eo&ab_channel=BusinessInsider")

video_options = yt.streams.filter(adaptive=True)
#print(video_options)

video_options2 = yt.streams.filter(file_extension='mp4')
#print(video_options2)

to_download = video_options[0]
#print(to_download)

#to_download.download("/Users/Egg/Desktop/Youtube Downloads")

s = Search("Being Productive by doing nothing")

caption = yt.captions['en-US']
caption2 = caption.xml_captions
print(caption.generate_srt_captions())