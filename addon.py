import xbmcaddon
import xbmcgui
import xbmc
import os
import time
import random

addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

mediasource = '/mnt/braavos/photo/_slideshow/'
format_picture = ['.jpg','.gif','.png','.jpeg']
format_video = ['.mpg','.avi','.mp4']
#format_playlist = ['.m3u']
format_all = format_picture + format_video #+ format_playlist
picture_duration = 5000

while True:
 files = os.listdir(mediasource)
 random.shuffle(files)

 for file in files:
  file_name, file_extension = os.path.splitext(file)
  full_filepath = mediasource + file

  if file_extension in format_all:
   xbmc.executebuiltin('Notification(Present:,'+file+',3000)')

   if file_extension in format_picture:
    xbmc.executebuiltin('ShowPicture('+full_filepath+')')
    xbmc.sleep(picture_duration)

   if file_extension in format_video:
    xbmc.executebuiltin('xbmc.PlayMedia('+full_filepath+',noresume)')
    video_duration=int(xbmc.Player().getTotalTime())
    video_duration = video_duration * 1000
    xbmc.sleep(video_duration)

#   if file_extension in format_playlist:
#    xbmc.executebuiltin('xbmc.PlayMedia('+full_filepath+')')

