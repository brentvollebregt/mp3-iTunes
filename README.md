# mp3-iTunes
Downloads selected song from a iTunes album using YouTube as an audio source.

# Requirements
* Python (tested with 3.5)
* mutagen (pip install mutagen)
* youtube_dl (pip install youtube_dl)
* BeautifulSoup4 (pip install beautifulsoup4)
* PYQT5 (pip install pyqt5)
* ffmpeg (described in Installation#4+5)

# Installation
1. Make sure requirements are installed
2. Go to [http://ffmpeg.zeranoe.com/builds/](http://ffmpeg.zeranoe.com/builds/) and download ffmpeg.
3. Extract the files and copy ffmpeg.exe, ffplay.exe abd ffprobe.exe from the /bin folder to the location of spotify_album_downloader.py

# Usage
1. Go to the browser version of iTunes and find the album your desired song is in (e.g. [https://itunes.apple.com/nz/album/wolves/id1227716339](https://itunes.apple.com/nz/album/wolves/id1227716339) and copy the url.
2. Run spotify_album_downloader.py and insert the iTunes url and the number of the song in the album.
3. Click get data
4. Change tag details if needed
5. Click open search and copy a youtube url with good audio quality that has your desired song.
3. Click download. Files will be saved to /output/ in the cwd.

# Notes
You do what you want with this project, I will not be held liable for any troubles you may face from this