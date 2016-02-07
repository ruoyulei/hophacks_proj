import subprocess
import sys, errno
import signal 

print "hello"
#str = "youtube-dl http://www.youtube.com/watch?v=OC83NA5tAGE -qo - | mplayer -monitorpixelaspect 0.5 - &> /dev/null"
#subprocess.call(["bash","b.sh","&>","/dev/null"])

id = raw_input()
subprocess.call(["bash","a.sh",id,"&>","/dev/null"])
