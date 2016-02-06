#!/bin/bash
youtube-dl http://www.youtube.com/watch?v=$1 -qo - | mplayer -geometry 500x1+400+400 -monitorpixelaspect 0.5 - &> /dev/null
