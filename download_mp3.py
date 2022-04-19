# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import youtube_dl
import os



class Download(object):
  def __init__(self, url):
    self.url = url
    self.save_path = os.path.join(os.path.expanduser('~'), 'Download')
    self.song()

  def song(self):
    opts = {
        'verbose': True,
        'fixup' : 'detect_or_warn',
        'format' : 'bestaudio/best',
        'postprocessors': [{
            'key' : 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '1411'
        }],

        'extraction' : True,
        'outtmpl' : self.save_path + '/%(title)s.%(ext)s',
        'noplaylist' : True
    }

    ydl = youtube_dl.YoutubeDL(opts)
    ydl.download([self.url])

if __name__ == '__main__':
  url = input("silahkan paste linknya haha ^_^ \n")
  Download(url)

print("Thanks For Using this code -Radit")