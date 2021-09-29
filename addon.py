import xbmcaddon
import xbmcgui
import xbmc
import os
import time
import random

#set const
format_picture = ['.jpg','.gif','.png','.jpeg']
format_video = ['.mpg','.avi','.mp4']
format_playlist = ['.m3u']

#get addon information
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')


#LANGUAGE     = addon.getLocalizedString
#xbmcgui.Dialog().ok(LANGUAGE)

mediasource = addon.getSetting('mediasource')

format_all = ['']
if addon.getSetting('supportpictures') == 'true': format_all = format_all + format_picture
if addon.getSetting('supportvideos') == 'true': format_all = format_all + format_video
if addon.getSetting('supportplaylists') == 'true': format_all = format_all + format_playlist

picture_duration = int(addon.getSetting('picturedurantion')) * 1000

#xbmcgui.Dialog().ok('Print',str(picture_duration))

while True:
 files = os.listdir(mediasource)
 random.shuffle(files)

 for file in files:
  file_name, file_extension = os.path.splitext(file)
  full_filepath = mediasource + file

  if file_extension in format_all:
   xbmc.executebuiltin('Notification('','+file+',3000)')

   if file_extension in format_picture:
    xbmc.executebuiltin('ShowPicture('+full_filepath+')')
    xbmc.sleep(picture_duration)

   if file_extension in format_video:
    xbmc.executebuiltin('xbmc.PlayMedia('+full_filepath+',noresume)')
    xbmc.sleep(2000)
#    try:
    video_duration = int(xbmc.Player().getTotalTime())
    video_duration = video_duration * 1000
    xbmc.sleep(video_duration)
#    except:
#	 1=1

#   if file_extension in format_playlist:
#    xbmc.executebuiltin('xbmc.PlayMedia('+full_filepath+')')

