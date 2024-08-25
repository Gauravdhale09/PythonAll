import pytube
# Reading the above Taken movie Youtube link
video = "https://youtu.be/-LIIf7E-qFI"
data = pytube.YouTube(video)
# Converting and downloading as 'MP4' file
audio = data.streams.get_audio_only()
audio.download()
