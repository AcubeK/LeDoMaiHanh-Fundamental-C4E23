from youtube_dl import YoutubeDL

#download ut vids
dl = YoutubeDL()
dl.download(['https://www.youtube.com/watch?v=WkVvG4QTO9M', 'https://www.youtube.com/watch?v=iX-QaNzd-0Y'])

#download audios
options = {
    'format': 'bestaudio/audio' # Tell the downloader to download only the best quality of audio
}
dl = YoutubeDL(options)
dl.download(['https://www.youtube.com/watch?v=c3jHlYsnEe0', 'https://www.youtube.com/watch?v=84znrPmOePc'])

# search and download the first video
options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': 1 # Tell downloader to download only the first entry (video)
}
dl = YoutubeDL(options)
dl.download(["James Young - I'll be good"])

# search and download the first audio
options = {
    'default_search': 'ytsearch', 
    'max_downloads': 1, 
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(['Aaron Smith - Dancin KRONO Remix'])