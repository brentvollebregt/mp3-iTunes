from __future__ import unicode_literals
import youtube_dl
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, error, TYER
from mutagen.easyid3 import EasyID3
import os
from bs4 import BeautifulSoup
import urllib.request
import webbrowser
import json

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if '_percent_str' in d:
        if d['status'] == 'downloading':
            ui.SetStaus(d['_percent_str'])
    if d['status'] == 'finished':
        ui.SetStaus('Done downloading, now converting ...')
        print ('Done downloading, now converting ...')

def downloadYoutubeToMP3(link):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
            }],
            'logger': MyLogger(),
            'progress_hooks': [my_hook]
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            a = ydl.download([link])
        return True
    except Exception as e:
        print (e)
        return False


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(532, 320)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("PythonIcon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEditItunesURL = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditItunesURL.setGeometry(QtCore.QRect(50, 10, 381, 20))
        self.lineEditItunesURL.setObjectName("lineEditItunesURL")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 31, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 41, 16))
        self.label_2.setObjectName("label_2")
        self.spinBoxItunesTrack = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBoxItunesTrack.setGeometry(QtCore.QRect(50, 40, 61, 21))
        self.spinBoxItunesTrack.setMinimum(1)
        self.spinBoxItunesTrack.setObjectName("spinBoxItunesTrack")
        self.pushButtonGetData = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonGetData.setGeometry(QtCore.QRect(440, 10, 81, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonGetData.setFont(font)
        self.pushButtonGetData.setObjectName("pushButtonGetData")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 60, 511, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 51, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 51, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 120, 51, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 140, 51, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 160, 51, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 180, 51, 16))
        self.label_8.setObjectName("label_8")
        self.lineEditTitle = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditTitle.setGeometry(QtCore.QRect(60, 80, 331, 20))
        self.lineEditTitle.setObjectName("lineEditTitle")
        self.lineEditAlbum = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditAlbum.setGeometry(QtCore.QRect(60, 100, 331, 20))
        self.lineEditAlbum.setObjectName("lineEditAlbum")
        self.lineEditArtist = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditArtist.setGeometry(QtCore.QRect(60, 120, 331, 20))
        self.lineEditArtist.setObjectName("lineEditArtist")
        self.lineEditTrack = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditTrack.setGeometry(QtCore.QRect(60, 140, 331, 20))
        self.lineEditTrack.setObjectName("lineEditTrack")
        self.lineEditYear = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditYear.setGeometry(QtCore.QRect(60, 160, 331, 20))
        self.lineEditYear.setObjectName("lineEditYear")
        self.lineEditGenre = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditGenre.setGeometry(QtCore.QRect(60, 180, 331, 20))
        self.lineEditGenre.setObjectName("lineEditGenre")
        self.labelAlbumArt = QtWidgets.QLabel(self.centralwidget)
        self.labelAlbumArt.setGeometry(QtCore.QRect(400, 80, 121, 121))
        self.labelAlbumArt.setFrameShape(QtWidgets.QFrame.Box)
        self.labelAlbumArt.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelAlbumArt.setLineWidth(1)
        self.labelAlbumArt.setText("")
        self.labelAlbumArt.setObjectName("labelAlbumArt")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 200, 511, 21))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(6, 220, 61, 16))
        self.label_18.setObjectName("label_18")
        self.lineEditVideoDownloadURL = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditVideoDownloadURL.setGeometry(QtCore.QRect(70, 220, 361, 20))
        self.lineEditVideoDownloadURL.setObjectName("lineEditVideoDownloadURL")
        self.pushButtonOpenYTSearch = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonOpenYTSearch.setGeometry(QtCore.QRect(440, 220, 81, 23))
        self.pushButtonOpenYTSearch.setObjectName("pushButtonOpenYTSearch")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(10, 240, 511, 21))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.pushButtonStart = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonStart.setGeometry(QtCore.QRect(10, 260, 511, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonStart.setFont(font)
        self.pushButtonStart.setObjectName("pushButtonStart")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButtonGetData.clicked.connect(self.ButtonGetData)
        self.pushButtonStart.clicked.connect(self.ButtonStart)
        self.pushButtonOpenYTSearch.clicked.connect(self.ButtonOpenSearch)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MP3 Download and Tagger"))
        self.lineEditItunesURL.setPlaceholderText(_translate("MainWindow", "URL of Itunes Album"))
        self.label.setText(_translate("MainWindow", "URL:"))
        self.label_2.setText(_translate("MainWindow", "Track:"))
        self.pushButtonGetData.setText(_translate("MainWindow", "Get Data"))
        self.label_3.setText(_translate("MainWindow", "Title:"))
        self.label_4.setText(_translate("MainWindow", "Album:"))
        self.label_5.setText(_translate("MainWindow", "Artist:"))
        self.label_6.setText(_translate("MainWindow", "Track:"))
        self.label_7.setText(_translate("MainWindow", "Year:"))
        self.label_8.setText(_translate("MainWindow", "Genre:"))
        self.lineEditTitle.setPlaceholderText(_translate("MainWindow", "Song Title"))
        self.lineEditAlbum.setPlaceholderText(_translate("MainWindow", "Song Album"))
        self.lineEditArtist.setPlaceholderText(_translate("MainWindow", "Song Artist"))
        self.lineEditTrack.setPlaceholderText(_translate("MainWindow", "Song Track No."))
        self.lineEditYear.setPlaceholderText(_translate("MainWindow", "Song Year"))
        self.lineEditGenre.setPlaceholderText(_translate("MainWindow", "Song Genre"))
        self.label_18.setText(_translate("MainWindow", "Video URL:"))
        self.lineEditVideoDownloadURL.setPlaceholderText(_translate("MainWindow", "URL to YouTube Video"))
        self.pushButtonOpenYTSearch.setText(_translate("MainWindow", "Open Search"))
        self.pushButtonStart.setText(_translate("MainWindow", "Download"))

    def ButtonGetData(self):
        self.lineEditVideoDownloadURL.clear()
        self.SetStaus("Downlaoding webpage")
        response = urllib.request.urlopen(self.lineEditItunesURL.text())
        file = (response.read()).decode('utf-8')
        soup = BeautifulSoup(file, 'html.parser')
        self.SetStaus("Parasing webpage")

        json_data = json.loads(soup.find('script', type='fastboot/shoebox').text)
        album_title = json_data['data']['attributes']['name']
        genre = [i['attributes']['name'] for i in json_data['included'] if i['type'] == 'genre'][0]
        song_raw = [i for i in json_data['included'] if i['type'] == 'song' and i['attributes']['trackNumber'] == self.spinBoxItunesTrack.value()][0]
        Focus_song_data = [song_raw['attributes']['name'],
                           album_title,
                           song_raw['attributes']['artistName'],
                           str(song_raw['attributes']['trackNumber']),
                           song_raw['attributes']['releaseDate'].split('-')[0],
                           genre]

        image_id = json_data['data']['relationships']['artwork']['data']['id']
        image = [i['attributes']['url'] for i in json_data['included'] if i['type'] == 'image' and i['id'] == image_id][0]
        Image_URL = image.replace('{w}', '500').replace('{h}', '500').replace('{f}', 'jpg')
        self.SetStaus("Downloading album art")
        urllib.request.urlretrieve(Image_URL, (os.getcwd() + "/TempAArtImage.jpg"))
        self.SetStaus("Appending tags to UI")
        self.labelAlbumArt.setPixmap(QtGui.QPixmap(os.getcwd() + "/TempAArtImage.jpg").scaled(self.labelAlbumArt.size(), QtCore.Qt.KeepAspectRatio))
        self.lineEditTitle.setText(Focus_song_data[0])
        self.lineEditAlbum.setText(Focus_song_data[1])
        self.lineEditArtist.setText(Focus_song_data[2])
        self.lineEditTrack.setText(Focus_song_data[3])
        self.lineEditYear.setText(Focus_song_data[4].split(" ")[-1])
        self.lineEditGenre.setText(Focus_song_data[5])
        self.SetStaus("Data scraped")

    def ButtonStart(self):
        self.SetStaus("Downloading")
        a = downloadYoutubeToMP3(self.lineEditVideoDownloadURL.text())
        if not a:
            self.SetStaus("Donwload Error")
            return
        self.SetStaus("Searching for file")
        files_in_cd = os.listdir(os.getcwd())
        for i in files_in_cd:
            if i.endswith(".mp3"):
                file = os.getcwd() + "\\" + i
        self.SetStaus("Tagging " + file)


        self.SetStaus("Setting album art")
        audio = MP3(file, ID3=ID3)
        try:
            audio.add_tags()
        except error:
            pass
        audio.tags.add(APIC(encoding=3, mime='image/jpeg', type=3, desc=u'cover', data=open(os.getcwd() + "/TempAArtImage.jpg", 'rb').read()))
        audio.save()
        self.SetStaus("Setting tags")
        audio = EasyID3(file)
        audio["tracknumber"] = self.lineEditTrack.text()
        audio["title"] = self.lineEditTitle.text()
        audio["album"] = self.lineEditAlbum.text()
        audio["artist"] = self.lineEditArtist.text()
        audio["genre"] = self.lineEditGenre.text()
        audio.save()

        audio = ID3(file)
        audio.add(TYER(encoding=3, text=(self.lineEditYear.text())))
        audio.save()

        self.SetStaus("Renaming and moving song")
        title = self.lineEditTitle.text().strip('/\\:*?"><|')
        artist = self.lineEditArtist.text().strip('/\\:*?"><|')
        if not os.path.exists(os.getcwd() + "/output/"):
            os.makedirs(os.getcwd() + "/output/")
        try:
            os.rename(file, (os.getcwd() + "/output/" + artist + " - " + title + ".mp3"))
            self.SetStaus("Saved at: " + os.getcwd() + "/output/" + artist + " - " + title + ".mp3")
        except:
            self.SetStaus("Could not rename. File saved at: " + os.getcwd() + "/temp/song.mp3")
        os.remove(os.getcwd() + "/TempAArtImage.jpg")


    def ButtonOpenSearch(self):
        search_term = self.lineEditArtist.text() + " " + self.lineEditTitle.text() + " lyrics"
        webbrowser.open("https://www.youtube.com/results?search_query=" + '+'.join(search_term.split(" ")))

    def SetStaus(self, message):
        self.statusbar.showMessage("Status:    " + message)


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
