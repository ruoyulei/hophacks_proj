import sys
import os
import subprocess

#f = open('/dev/null', 'w')

#print "hello"
str = "youtube-dl http://www.youtube.com/watch?v=OC83NA5tAGE -qo - | mplayer -monitorpixelaspect 0.5 -"
subprocess.call(str, shell=True)




#str2 = "youtube-dl http://www.youtube.com/watch?v=OC83NA5tAGE -o - | mplayer -monitorpixelaspect 0.5 - &> /dev/null"

#arr = ["youtube-dl", "http://www.youtube.com/watch?v=BJ0xBCwkg3E", "-wio", "-", "|", "mplayer", "-vo", "-monitorpixelaspect", "0.5", "-"]

#call(arr)



#ps = subprocess.Popen(("youtube-dl", "http://www.youtube.com/watch?v=BJ0xBCwkg3E", "-o", "-"), stdout=subprocess.PIPE)
#output = subprocess.check_output(("mplayer", "-vo", "-monitorpixelaspect", "0.5", "-"), stdin=ps.stdout)
#ps.wait()